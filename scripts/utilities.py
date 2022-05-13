
import pandas as pd

def format_float(value):
    return f'{value:,.2f}'

def convert_ms_to_hrs(df,col_name):
    """ This function converts millisecond to hours"""
    hr = 3600000
    df[col_name+" in hrs"] = df[col_name] / hr
    
    return df[col_name+" in hrs"]


def find_agg(df:pd.DataFrame, agg_column:str, wanted_col:str,agg_metric:str, col_name:str, top:int, order=False )->pd.DataFrame:
    """ This function calculates aggregate of column """
    new_df = df.groupby(agg_column)[wanted_col].agg(agg_metric).reset_index(name=col_name).\
    sort_values(by=col_name, ascending=order)[:top]
    
    return new_df

def convert_bytes_to_megabytes(df,col):
    """ This function converts bytes to Megabytes"""
    megabyte = 1*10e+5
    df[col+"in MB"] = df[col] / megabyte
    
    return df[col+"in MB"]

def find_total_volume(df,app_names):
    """ This function calculates the total data volume each application"""
    for app_name in app_names:
        df[app_name+' total volume (Bytes)'] = df[app_name+' DL (Bytes)']+df[app_name+' UL (Bytes)']
    return df

pd.options.display.float_format = format_float