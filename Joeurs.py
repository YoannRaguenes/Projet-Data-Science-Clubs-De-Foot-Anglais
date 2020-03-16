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
#PROBLEME AVEC RECUPERATION DU TABLEAU 