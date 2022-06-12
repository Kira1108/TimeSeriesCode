import pandas as pd
import numpy as np

def calculate_return(df:pd.DataFrame, price_col:str = "close"):
    df['net_return'] = df[price_col].pct_change()
    df['gross_return'] = df['net_return'] + 1
    df['log_return'] = np.log(df['gross_return'])
    return df