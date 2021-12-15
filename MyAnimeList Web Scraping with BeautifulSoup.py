import requests
from bs4 import BeautifulSoup
import numpy as np

url = input('Paste a MAL url: ')
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

original_name = soup.find(class_='title-name h1_bold_none').text
japanese_name = soup.find(class_='title-english title-inherit').text
episodes = soup.find(id='curEps')
episodes = ('{} Episodes'.format(episodes.text))
score = soup.find(class_='fl-l score')
score = ('{}/10'.format(score.text))
rank = soup.find(class_='numbers ranked').text
popularity = soup.find(class_='numbers popularity').text
members = soup.find(class_='numbers members').text
season = soup.find(class_='information season').text
studio = soup.find(class_='information studio author').text

print(original_name)
print(japanese_name)
print(episodes)
print(score)
print(rank)
print(popularity)
print(members)
print(season)
print(studio)

info = [original_name, japanese_name, episodes, score, rank, popularity, members, season, studio]

import pandas as pd

df = pd.DataFrame(info)
df.to_csv('Anime Info.csv')
print('CSV Created')
