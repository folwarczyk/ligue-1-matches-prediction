# -*- coding: utf-8 -*-
"""ligue1-web-scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WrD2GlV7xYLiUlKFA_XSbU-5ZsOyBR3A
"""

import requests

#url = "https://fbref.com/en/comps/13/Ligue-1-Stats"
url = "https://fbref.com/en/comps/13/2021-2022/2021-2022-Ligue-1-Stats"

#download the page
#get method will make a request to the server and download htm of the page
data = requests.get(url)

#look at the html
data.text

#library to parse html
from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text)

#select the stats table and then select all the a tags with the links that we want inside the table
#[0] - first element in the list
standings_table = soup.select('table.stats_table')[0]

standings_table
#now we only have html for the table

#finding all of the a tags inside the table
links = standings_table.find_all('a')

[l.get("href") for l in links ]

links = [l.get("href") for l in links if '/squads/' in l.get("href")]

links

team_url = [f"https://fbref.com{l}" for l in links]

team_url

team_url = team_url[0]

data = requests.get(team_url)

data.text

import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
# %pip install lxml

matches = pd.read_html(data.text, match="Scores & Fixtures")

matches[0].head(5)

soup = BeautifulSoup(data.text)

links = soup.find_all('a')

links = [l.get("href") for l in links]

links = [l for l in links if l and 'all_comps/shooting' in l]

links

data = requests.get(f"https://fbref.com{links[0]}")

data.text

shootings = pd.read_html(data.text, match="Shooting")[0]

shootings.head()

shootings.columns = shootings.columns.droplevel()

shootings.head()

matches[0].head()

#merge 2 dataframes (matches and shoortings)
team_data = matches[0].merge(shootings[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")

team_data.head()

team_data

matches[0].shape

shootings.shape

#a for loop
years = list(range(2023, 2018, -1))

years

all_matches = []

standings_url = "https://fbref.com/en/comps/13/Ligue-1-Stats"

import time

for year in years:
    data = requests.get(standings_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    standings_tables = soup.select('table.stats_table')

    if not standings_tables:
        continue
    standings_table = standings_tables[0]

    links = [l.get("href") for l in standings_table.find_all('a')]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]

    previous_season = soup.select("a.prev")[0].get("href")
    standings_url = f"https://fbref.com{previous_season}"

    for team_url in team_urls:
        team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
        data = requests.get(team_url)
        soup = BeautifulSoup(data.text, 'html.parser')

        scores_and_fixtures_section = soup.find('span', {'data-label': 'Scores & Fixtures'})
        if scores_and_fixtures_section is None:
            continue
        scores_and_fixtures_table = scores_and_fixtures_section.find_next('table')

        matches = pd.read_html(str(scores_and_fixtures_table))[0]

        links = [l.get("href") for l in soup.find_all('a')]
        links = [l for l in links if l and 'all_comps/shooting/' in l]

        try:
            data = requests.get(f"https://fbref.com{links[0]}")
            shootings = pd.read_html(data.text, match="Shooting")[0]
            shootings.columns = shootings.columns.droplevel()

            team_data = matches.merge(shootings[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
            team_data = team_data[team_data["Comp"] == "Ligue 1"].copy()
            team_data.loc[:, "Season"] = year
            team_data.loc[:, "Team"] = team_name
            all_matches.append(team_data)
        except (ValueError, IndexError):
            continue

        time.sleep(1)

len(all_matches)

match_df = pd.concat(all_matches)

match_df.columns = [c.lower() for c in match_df.columns]

match_df

match_df.to_csv("ligue-1-matches.csv")

!ls

from google.colab import files
files.download('ligue-1-matches.csv')