import sys
import os

if __name__ ==  '__main__':
    path = os.path.dirname(os.path.abspath('Main_sqlite.py'))+'\\'
    sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]), f"{path}Scripts"))
    
    import Database_tables_and_queries_created as create
    
    DB = f'{path}Used_files\\Spotify_analysis.db'
    input_path_files = f'{path}Spotify_results\\'
    output_path_files = f'{path}Queries_results\\'
    if not os.path.exists(output_path_files):
        os.makedirs(output_path_files)
    
    file_name = f'{path}Used_files\\queries.txt'

    create.createDB(DB)
    create.create_all_tables(DB, input_path_files)
    create.creating_data(DB, file_name, output_path_files)