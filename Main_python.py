import sys
import os

if __name__ ==  '__main__':
    path = os.path.dirname(os.path.abspath('Main_python.py'))+'\\'
    sys.path.insert(0, os.path.join(os.path.dirname(sys.path[0]), f"{path}Scripts"))
    
    import Spotify_data_extraction as SDE
    from Getting_access_to_SpotifyAPI import get_token
    
    output_path = f'{path}Spotify_results\\'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    #Set the timezone where your music was played
    utc_hours_diff = -6
    
    SH = SDE.Get_StreamingHistory(f'{path}Used_files\\StreamingHistory_music_0.json', utc_hours_diff)
    Songs_info = SDE.Collecting_StreamingHistory_details(get_token(), SH)
    SH_complementary_info = SDE.Collecting_StreamingHistory_details_2(get_token(), SH, Songs_info)
    SH_dataframes_generated = SDE.Get_sources_songs(get_token(), SH_complementary_info)
    SDE.Printing_metrics(SH, SH_complementary_info)
    SDE.Generate_files(output_path, SH_complementary_info, SH_dataframes_generated)