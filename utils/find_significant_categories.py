import pandas as pd
def find_significant_categories(df, column, target_col, significance_threshold=2.0, mu=None, sigma=None):
    if not isinstance(df[column].dtype, pd.CategoricalDtype):
        df[column] = df[column].astype('category')

    if mu is None:
        mu = df[target_col].mean()
    if sigma is None:
        sigma = df[target_col].std()

    levels_df = df.groupby(column, observed=True).agg(
        n_=(target_col, 'size'),
        mean_=(target_col, 'mean'),
        std_=(target_col, 'std')
    )

    levels_df['z_'] = (levels_df['mean_'] - mu) / (levels_df['std_'] / np.sqrt(levels_df['n_']))
    
    important_levels = levels_df[
        levels_df['z_'].abs() > significance_threshold
    ].index.tolist()

    return important_levels