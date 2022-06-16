import numpy as np

def create_lag(l = 3, column = None):
    """create a function that transforms a dataframe column with lags
    Args:
        l: number of list, if a number is passed, transform to lag 0-l(inclusive)
            if a list is passed, transform lags specifed in the list
        column: column name to perform lag transformation

    Returns:
        a function that can be used to transform a dataframe
    
    """
    if isinstance(l, int):
        l = range(1, l + 1)
    def _create_lag(df):
        col = column if column is not None else df.columns[0]
        df = df.copy()
        for i in l:
            df[f'{col}_lag_{i}'] = df[col].shift(i)
        return df.dropna(how = 'any')
    return _create_lag

def log_transform(columns:list, plus:int = 0):
    """Perform log transformation of columns
    Args:
        columns: list of column names to perform log transformation
        plus: plus value to ensure non-negative values

    Returns:
        a function that can be used to transform a dataframe
    """
    if isinstance(columns, str):
        columns = [columns]
    def transform(df):
        df = df.copy()
        for col in df.columns:
            df[f'log_{col}'] = np.log(df[col] + plus)
        return df
    return transform

def train_test_split(test_size = 0.2, features:list = None, target:str = None):
    """Split data into train and test sets"""
    def split(df):
        split_point = int(df.shape[0] * (1 - test_size))
        train, test = df.iloc[:split_point], df.iloc[split_point:]
        if features is not None and target is not None:
            return train[features], test[features], train[target], test[target]
        return train, test
    return split