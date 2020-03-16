# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:42:36 2020

@author: Kévin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://fbref.com/fr/comps/34/stats/National-League-Stats")
html_soup = BeautifulSoup(html, "html.parser")
tab = html_soup.findAll("table", class_="min_width sortable stats_table", id="stats_standard_squads")
body = tab[0].findAll("tbody")
rows = body[0].findAll("tr")
print(len(rows))
teams = []
for row in rows:
    cells = row.findAll("a")
    cells2 = row.findAll("td")
    
    try:
        teams_entry = {
                "Nom d'équipe": cells[0].text,
                "Match joué" : cells2[1].text,
                "Buts marqués" : cells2[4].text,
                    }
        teams.append(teams_entry)
    except ValueError:
            print("Ouch!")
df = pd.DataFrame(teams)

print(df.head(24))