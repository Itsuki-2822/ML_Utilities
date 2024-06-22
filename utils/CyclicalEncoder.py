import pandas as pd
import numpy as np

def CyclicalEncoder(df,col):
    df['datetime'] = pd.to_datetime(df[col])

    df['year'] = df[col].dt.year
    df['month'] = df[col].dt.month
    df['day'] = df[col].dt.day
    df['hour'] = df[col].dt.hour
    df['minute'] = df[col].dt.minute
    df['second'] = df[col].dt.second
    df['dayofweek'] = df[col].dt.dayofweek

    df['hour_sin'] = np.sin(2 * np.pi * df['hour']/24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour']/24)
    
    def days_in_month(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            raise ValueError("Invalid month value")

    df['day_sin'] = df.apply(lambda row: np.sin(2 * np.pi * row['day'] / days_in_month(row['year'], row['month'])), axis=1)
    df['day_cos'] = df.apply(lambda row: np.cos(2 * np.pi * row['day'] / days_in_month(row['year'], row['month'])), axis=1)

    df['dayofweek_sin'] = np.sin(2 * np.pi * df['dayofweek']/7)
    df['dayofweek_cos'] = np.cos(2 * np.pi * df['dayofweek']/7)

    df.drop(['datetime','year'],axis=1,inplace=True)
    return df