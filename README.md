Thank you for your interest in my project.

If you want to get the elements to recreate the dashboard, taking these points in considerations:

1. Once you have downloaded your own data, you will get a "my_spotify_data" zip file. The only file you are going to need from there is the "StreamingHistory_music_0" JSON file. Put this file into the "Used_files" folder.

2. In order to use the Spotify Web API, you will have to create an account in Spotify to developers and then create a project. Once made this, you need to replace the "client id" and "client secret" values from the ".env" file, ubicated in the "Used_files" folder, with your own alphanumeric codes. You can get these values clicking the "settings" button of your project.
   
3. If you have renamed the JSON file, you have to modify the 18th line of the "Main_python.py" script adding the new name of the file.

4. Spotify use the utc time zone, so you can modify the 16th line of the "Main_python.py" script replacing the value with your time zone difference. For example, I chose "-6" because I use the Mexico city time zone. If you agree with using the utc time zone, just adjust this value to 0.

5. Run the "Main_python.py" script. This going to create a "Spotify_results" folder with the excel files required.

6. Then, run the "Main_sqlite.py" script. This going to create a "Queries_results" folder with the excel files created by the sql queries. These are the files that you are going to use to recreate the dashboard.

If you want to add a new query, just write it at the bottom of the "queries.txt" file, respecting the order. If the Spotify Web API does not allow you make more calls, maybe you are exceeding the rate limit established by spotify (429 error). One way to solve this problem is creating another project and modifying the "client id" and "client secret" in the ".env", just as the 4 point mentioned before.

References:

Download your spotify data: https://www.spotify.com/us/account/privacy/

Spotify for developers: https://developer.spotify.com/
