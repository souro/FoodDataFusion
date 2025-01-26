import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GroupShuffleSplit, KFold
from iterstrat.ml_stratifiers import MultilabelStratifiedKFold

def load_data(path):
    return pd.read_parquet(path)

def preprocess_data(df):
    df.fillna({'description': '', 'image_path': None}, inplace=True)
    ...
    
    return df

def stratified_split(df, label_columns, test_size=0.2, random_state=42):
    X = df['image_path']
    y = df[label_columns]
    
    mskf = MultilabelStratifiedKFold(n_splits=5, shuffle=True, random_state=random_state)
    for train_index, test_index in mskf.split(X, y):
        train_df = df.iloc[train_index]
        test_df = df.iloc[test_index]
        break
    
    return train_df, test_df

def group_based_split(df, group_column, test_size=0.2, random_state=42):
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=random_state)
    groups = df[group_column]
    for train_idx, test_idx in splitter.split(df, groups=groups):
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]
    return train_df, test_df

def custom_split(df, label_columns):
    df['label_combination'] = df[label_columns].apply(lambda x: tuple(x), axis=1)
    splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_idx, test_idx in splitter.split(df, df['label_combination']):
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]
    df.drop('label_combination', axis=1, inplace=True)
    return train_df, test_df
