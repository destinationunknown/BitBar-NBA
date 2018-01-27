#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Title goes here</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Your Name</bitbar.author>
# <bitbar.dependencies>python</bitbar.dependencies>


import requests
from bs4 import BeautifulSoup

url = "http://www.basketball-reference.com/boxscores/"

teams = {'Atlanta': "ATL", 'Boston': "BOS", 'Brooklyn': 'BKN', 'Charlotte': 'CHA', 'Chicago': 'CHI',
         'Cleveland': 'CLE', 'Dallas': 'DAL', 'Denver': 'DEN', 'Detroit': 'DET', 'Golden State': 'GSW',
         'Houston': 'HOU', 'Indiana': 'IND', 'LA Clippers': 'LAC', 'LA Lakers': 'LAL', 'Memphis': 'MEM',
         'Miami': 'MIA', 'Milwaukee': 'MIL', 'Minnesota': 'MIN', 'New Orleans': 'NOP', 'New York': 'NYK',
         'Oklahoma City': 'OKC', 'Orlando': 'ORL', 'Philadelphia': 'PHI', 'Phoenix': 'PHX',
         'Portland': 'POR', 'Sacramento': 'SAC', 'San Antonio': 'SAS', 'Toronto': 'TOR', 'Utah': 'UTA',
         'Washington': 'WAS'}

teams_fav = {'GSW', 'OKC'}

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")


print "NBA"
print "---"


# Example game = "OKC 108 - CLE 103"
games_compact = ""

for game in soup.find_all("table", class_="teams"):
    winner = game.find("tr", class_="winner").find("a").text
    winner_score = game.find("tr", class_="winner").find("td", class_="right").text
    loser = game.find("tr", class_="loser").find("a").text
    loser_score = game.find("tr", class_="loser").find("td", class_="right").text
    #print winner + " " + winner_score + " - " + loser + " " + loser_score

    #   print type(teams.get(winner))
    games_compact += teams.get(winner)
    games_compact += " "
    games_compact += winner_score
    games_compact += " - "
    games_compact += teams.get(loser)
    games_compact += " "
    games_compact += loser_score
    #games_compact += ", "
    print games_compact
    print "---"
    games_compact = ""


# Remove the last two characters of games_compact:
games_compact = games_compact[:-3]
#print games_compact
#print str(games_unfiltered)