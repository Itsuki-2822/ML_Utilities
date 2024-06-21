import pandas as pd

def compare_categorical_columns(df_train, df_test, exclude_columns=None, detail=False):
    exclude_columns = [] if exclude_columns is None else exclude_columns

    categorical_columns = df_train.select_dtypes(include='object').columns
    categorical_columns = [col for col in categorical_columns if col not in exclude_columns]
    
    results = []
    for col in categorical_columns:
        train_unique = set(df_train[col].unique())
        test_unique = set(df_test[col].unique())
        
        common_values = train_unique & test_unique
        unique_to_train = train_unique - test_unique
        unique_to_test = test_unique - train_unique
        
        results.append({'column': col,'common_values': len(common_values),'unique_to_train': len(unique_to_train),'unique_to_test': len(unique_to_test)})
    
    summary_df = pd.DataFrame(results)

    details = {}
    if detail:
        for col in categorical_columns:
            train_unique = set(df_train[col].unique())
            test_unique = set(df_test[col].unique())
            
            common_values = train_unique & test_unique
            unique_to_train = train_unique - test_unique
            unique_to_test = test_unique - train_unique
            
            details[col] = {
                'common_values': list(common_values),
                'unique_to_train': list(unique_to_train),
                'unique_to_test': list(unique_to_test)
            }

    def display_detailed_info(col_name):
        if col_name in details:
            detail_info = details[col_name]
            max_len = max(len(detail_info['common_values']), len(detail_info['unique_to_train']), len(detail_info['unique_to_test']))
            detail_df = pd.DataFrame({
                'common_values': pd.Series(detail_info['common_values']).reindex(range(max_len)),
                'unique_to_train': pd.Series(detail_info['unique_to_train']).reindex(range(max_len)),
                'unique_to_test': pd.Series(detail_info['unique_to_test']).reindex(range(max_len))
            })
            return detail_df
        else:
            return "No detailed information available for column: {}".format(col_name)
    
    return summary_df, display_detailed_info


#summary_df, display_detailed_info = analyze_category_differences(df_train, df_test, exclude_columns = False, detail=True)
#detail_df = display_detailed_info('home_team')
