# My spotify journey
Thank you for your interest in my work. This project was made with the intention of making a more in-depth analyzis about my streaming history data, similar to the "Spotify wrapped" but taking in consideration aspects like albums, the release year of the music that I listen, my activity throughout the day, etc.

If you want to get the elements to recreate the dashboard, taking these points in considerations:

## Get your own spotify data
In the "References" section you will find a link to request your streaming history data. You will be able to download your data in a timelapse of five days approximately. Once you have downloaded your data, you will get a "my_spotify_data" zip file. The only file that you will need from there is the "StreamingHistory_music_0" JSON file.

## Create an account in spotify for developers
In order to use the Spotify Web API, you will have to create an account in Spotify to developers. In the "References" section you will find a link where you can log in with your spotify account. If you click into your username a drop-down list will appear, just click "dashboard". There you can create an app. At the moment of creating your app, in the "Which API/SDKs are you planning to use?" section only select the "Web API" option, the rest of them will not be necessary. If you do not know what to put in the "Redirect URIs" section, I recommend you fill this field like this: "http://localhost:1410/" (excluding the commas). Once you have created your app, go to "settings", copy the "Client ID" and "Client secret" and then replace them in the "Used files" folder.

## Folders
### Used files
This folder contains two files: a ".env" file where your credentials will be stored and a text file "queries.txt" that contains all the queries used to create the dashboard. 
## Scripts
1. Getting_access_to_SpotifyAPI.py: This script contains two functions: "get_token" returns a token based on your credentials and the "get_auth_header" returns the authentication to required to use the API.
2. Spotify_utilities: This script acts like a 
