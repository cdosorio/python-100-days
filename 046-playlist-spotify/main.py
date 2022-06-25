from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

clientID = "1234"
clientSecret = "1234"

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

desired_date = "2000-08-12" #input("Which year do you want travel to? Use format YYYY-MM-DD:\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{desired_date}/")
billboard_chart_page = response.text
soup = BeautifulSoup(billboard_chart_page, 'html.parser')

top_100_songs_names = soup.find_all(name="h3", class_="u-letter-spacing-0021", id="title-of-a-story")
top_100_songs_names = [song.text.strip() for song in top_100_songs_names]
top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Songwriter(s):')
top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Producer(s):')
top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Imprint/Promotion Label:')

top_100_songs_artist = soup.find_all(name="span", class_="u-letter-spacing-0021")
top_100_songs_artist = [artist.text.strip() for artist in top_100_songs_artist]
