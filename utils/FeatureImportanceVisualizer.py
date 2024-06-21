import matplotlib.pyplot as plt
import pandas as pd
import shap
from PermutationFeatureSelector import PermutationFeatureSelector

class FeatureImportanceVisualizer:
    def __init__(self, model, X_train, y_train, X_test, y_test):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def plot_feature_importance(self, figsize=(12, 10)):
        feature_importances = self.model.feature_importance(importance_type='gain')
        feature_names = self.X_train.columns
        feature_imp_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': feature_importances
        }).sort_values(by='Importance', ascending=False)
        plt.figure(figsize=figsize)
        plt.barh(feature_imp_df['Feature'], feature_imp_df['Importance'])
        plt.xlabel('Importance')
        plt.ylabel('Feature')
        plt.title('Feature Importance')
        plt.gca().invert_yaxis()
        plt.show()

    def plot_shap_importance(self, figsize=(12, 10)):
        explainer = shap.TreeExplainer(self.model)
        shap_values = explainer.shap_values(self.X_train)
        plt.figure(figsize=figsize)
        shap.summary_plot(shap_values, self.X_train, plot_type="bar", show=False)
        plt.show()

    def plot_permutation_importance(self, figsize=(12, 10)):
        permutation_importance = PermutationFeatureSelector(self.model, self.X_test, self.y_test, metric='rmse', random_state=28)
        permutation_importance.plot_permutation_importance(figsize=figsize, positive_color='blue', negative_color='red')

    def plot_all(self, figsize=(12, 10)):
        self.plot_feature_importance(figsize)
        self.plot_shap_importance(figsize)
        self.plot_permutation_importance(figsize)



#visualizer = FeatureImportanceVisualizer(model, X_train, y_train, X_test, y_test)
#visualizer.plot_all(figsize=(12, 10))
