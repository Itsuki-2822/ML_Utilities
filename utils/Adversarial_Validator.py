import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, KFold, train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import shap

class AdversarialValidator:
    def __init__(self, params=None, n_splits=5, random_state=28):
        if params is None:
            params = {
                'objective': 'binary',
                'boosting_type': 'gbdt',
                'metric': 'auc',
                'verbose': -1
            }
        self.params = params
        self.n_splits = n_splits
        self.random_state = random_state
        self.label_encoders = {}
        self.evals_result = {}
        self.boosters = []

    def preprocess_data(self, df_train, df_test, exclude_columns):
        df_train['is_train'] = 1
        df_test['is_train'] = 0

        df = pd.concat([df_train, df_test])
        df.drop(exclude_columns, axis=1, inplace=True)

        categorical_features = [col for col in df.columns if df[col].dtypes == 'object']
        for col in categorical_features:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.label_encoders[col] = le

        X = df.drop('is_train', axis=1)
        y = df['is_train']

        return X, y

    def train_and_evaluate(self, X, y, validation='stratifiedkfold', plot_feature_importance=True, plot_shap_summary=True):
        if validation == 'holdout':
            X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=self.random_state)
            train_data = lgb.Dataset(X_train, label=y_train)
            val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

            booster = lgb.train(
                self.params,
                train_data,
                valid_sets=[train_data, val_data],
                valid_names=['train', 'val'],
                num_boost_round=10000,
                callbacks=[lgb.early_stopping(stopping_rounds=100),
                           lgb.log_evaluation(period=100),
                           lgb.record_evaluation(self.evals_result)]
            )

            self.boosters.append(booster)
            self.plot_learning_curve(self.evals_result, metric='auc')
        
        elif validation == 'kfold':
            kf = KFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)
            for fold, (train_index, val_index) in enumerate(kf.split(X)):
                print(f"Training fold {fold + 1}")
                X_train, X_val = X.iloc[train_index], X.iloc[val_index]
                y_train, y_val = y.iloc[train_index], y.iloc[val_index]

                train_data = lgb.Dataset(X_train, label=y_train)
                val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

                booster = lgb.train(
                    self.params,
                    train_data,
                    valid_sets=[train_data, val_data],
                    valid_names=['train', 'val'],
                    num_boost_round=10000,
                    callbacks=[lgb.early_stopping(stopping_rounds=100),
                               lgb.log_evaluation(period=100),
                               lgb.record_evaluation(self.evals_result)]
                )

                self.boosters.append(booster)
                self.plot_learning_curve(self.evals_result, metric='auc')

        elif validation == 'stratifiedkfold':
            skf = StratifiedKFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)
            for fold, (train_index, val_index) in enumerate(skf.split(X, y)):
                print(f"Training fold {fold + 1}")
                X_train, X_val = X.iloc[train_index], X.iloc[val_index]
                y_train, y_val = y.iloc[train_index], y.iloc[val_index]

                train_data = lgb.Dataset(X_train, label=y_train)
                val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

                booster = lgb.train(
                    self.params,
                    train_data,
                    valid_sets=[train_data, val_data],
                    valid_names=['train', 'val'],
                    num_boost_round=10000,
                    callbacks=[lgb.early_stopping(stopping_rounds=100),
                               lgb.log_evaluation(period=100),
                               lgb.record_evaluation(self.evals_result)]
                )

                self.boosters.append(booster)
                self.plot_learning_curve(self.evals_result, metric='auc')

        if plot_feature_importance:
            self.plot_feature_importance()
        
        if plot_shap_summary:
            self.plot_shap_summary(X_train)

    def plot_learning_curve(self, evals_result, metric='auc'):
        plt.figure(figsize=(10, 5))
        plt.plot(evals_result['train'][metric], label='Train')
        plt.plot(evals_result['val'][metric], label='Validation')
        plt.xlabel('Iteration')
        plt.ylabel(metric)
        plt.title(f'Learning Curve ({metric})')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_feature_importance(self):
        feature_importance_df = pd.DataFrame()
        for i, booster in enumerate(self.boosters):
            fold_importance_df = pd.DataFrame()
            fold_importance_df["feature"] = booster.feature_name()
            fold_importance_df["importance"] = booster.feature_importance(importance_type='gain')
            fold_importance_df["fold"] = i + 1
            feature_importance_df = pd.concat([feature_importance_df, fold_importance_df], axis=0)

        feature_importance_df = feature_importance_df.groupby('feature').mean().sort_values(by="importance", ascending=False).reset_index()

        plt.figure(figsize=(12, 8))
        plt.barh(feature_importance_df['feature'], feature_importance_df['importance'])
        plt.xlabel("Feature Importance")
        plt.ylabel("Feature")
        plt.title("Feature Importance Across Folds")
        plt.gca().invert_yaxis()
        plt.show()

    def plot_shap_summary(self, X):
        explainer = shap.TreeExplainer(self.boosters[0]) 
        shap_values = explainer.shap_values(X)
        shap.summary_plot(shap_values, X, plot_type="bar")

    def predict(self, X):
        predictions = np.zeros(X.shape[0])
        for booster in self.boosters:
            predictions += booster.predict(X)
        predictions /= len(self.boosters)
        return predictions

#lgb_classifier = AdversarialValidator()
#X, y = lgb_classifier.preprocess_data(df_train, df_test, exclude_columns=False)
#lgb_classifier.train_and_evaluate(X, y, validation = 'holdout',plot_feature_importance=True, plot_shap_summary=True)
