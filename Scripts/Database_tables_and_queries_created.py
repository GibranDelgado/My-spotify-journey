import pandas as pd
import sqlite3 as sql
import glob
import os
from Getting_specific_query import specific_query, number_of_queries

def createDB(databaseName):
    conn = sql.connect(databaseName)
    conn.commit()
    conn.close()

def create_all_tables(databaseName, path_file):
    def create_and_fill_table(databaseName, df, tableName):
        dtypes = []
        
        for i, j in zip(df.columns, df.dtypes):
            if (j=='object' or j=='bool') and i!='startTime':
                dtypes.append('text')
            elif j=='int64':
                dtypes.append('integer')
            elif j=='float64':
                dtypes.append('numeric')
            else:
                dtypes.append('numeric')
        
        structure = pd.DataFrame({'columns': df.columns, 'dtypes': dtypes})
        columns_def = ''
        
        for k, row in structure.iterrows():
            columns_def += f'{row["columns"]} {row["dtypes"]}'
            if k!= len(structure) - 1:
                columns_def += ',\n' 
        
        sql_query = f'DROP TABLE IF EXISTS {tableName};\nCREATE TABLE {tableName}(\n' + columns_def + ')'
        
        conn = sql.connect(databaseName)
        cursor = conn.cursor()
        cursor.executescript(
            f"""{sql_query}"""
        )
        df.to_sql(tableName, conn, if_exists='replace', index=False)
        conn.commit()
        conn.close()
    
    ext = '.xlsx'
    csv_files = glob.glob(os.path.join(path_file,f'*{ext}'))
    
    for i in csv_files:
        create_and_fill_table(databaseName, pd.read_excel(i), f'{i[len(path_file):len(i)-len(ext)]}')

def execute_query(databaseName, query):
    conn = sql.connect(databaseName)
    cursor = conn.cursor()
    for row in cursor.execute(query):
        print(row)
    print('')
    conn.close()

def creating_data(databaseName, file_name, output_path_file):
    def generate_df(databaseName, query, file_name):
        conn = sql.connect(databaseName)
        df = pd.read_sql_query(query, conn)
        df.to_excel(file_name, index=False)
    
    n = number_of_queries(file_name)
    for i in range(1, n+1):
        out_file_name = f'{output_path_file}query_{i}.xlsx'
        generate_df(databaseName, specific_query(file_name,i), out_file_name)