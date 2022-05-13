import sqlite3
from sqlite3 import Error
import pandas as pd
import sys, getopt

def connection_DB():
    conn = sqlite3.connect("Db_files/user_analysis.db")
    cur = conn.cursor()
    return conn,cur

def create_table(table_name):
       
    create_query = " CREATE TABLE IF NOT EXISTS "+table_name+""" (user_id INTEGER PRIMARY KEY NOT NULL,
    engagement_score FLOAT DEFAULT NULL,
    experience_score FLOAT DEFAULT NULL,
    satisfaction_score FLOAT DEFAULT NULL)""" 
    conn, cur = connection_DB()
    cur.execute(create_query)
    conn.commit() 
    cur.close()

def insert_data(df: pd.DataFrame,table_name):
    conn, cur = connection_DB()
    for _,row in df.iterrows():
        insert_query = "INSERT INTO "+ table_name + """(user_id,engagement_score,
                                                        experience_score,satisfaction_score)values(?,?,?,?)"""
        to_be_inserted = (row[0],row[1],row[2],row[3])

        cur.execute(insert_query,to_be_inserted)
        conn.commit() 
    cur.close()

def fetch_data(table_name):
    conn, cur = connection_DB()
    colmn_names = []
    select_query = "select * FROM "+table_name
    values =cur.execute(select_query)
    for desc in cur.description:
        colmn_names.append(desc[0])

    conn.commit()
    df = pd.DataFrame(values, columns=colmn_names)
    cur.close()
    return df


if __name__ == '__main__':
    # df = pd.read_csv("../data/user_data_scores.csv")
    # insert_data(df,"user_scores")
    print(fetch_data("user_scores"))

    