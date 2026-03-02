import pandas as pd

def load_data(filepath):
    df = pd.read_excel(filepath)
    return df

def clean_transactions(df):
    df = df[df['CustomerID'].notnull()]
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df