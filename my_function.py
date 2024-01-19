import numpy as np
import pandas as pd
def clean_df(df):
    n_cols = []
    for i in range(len(df.columns)):
        n_cols.append(df.columns[i].lower().replace(' ', '_'))
    df.columns = n_cols
    df = df.rename(columns={'st':'state'})
    df = df.drop_duplicates()
    df = df.drop(1071, axis = 0)
    value_mapping = {'Cali': 'California','WA': 'Washington','AZ': 'Arizona'}
    df['state'] = df['state'].replace(value_mapping)
    df['gender']= df['gender'].fillna('F')
    df['gender']=np.where(df['gender'].isin(['F', 'female', 'Femal']),'F','M')
    df['customer_lifetime_value']=df['customer_lifetime_value'].str.replace('%','').astype(float)/100
    new_list = []
    for item in df['number_of_open_complaints']:
        new_list.append(item.split('/')[1])
    df['number_of_open_complaints']=new_list
    df['number_of_open_complaints']=pd.to_numeric(df['number_of_open_complaints'], errors = 'coerce')
    df['customer_lifetime_value']=pd.to_numeric(df['customer_lifetime_value'], errors='coerce')
    df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(df['customer_lifetime_value'].mean()).round(decimals = 2)
    
    return df