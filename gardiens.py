# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:40:04 2020

@author: Roshan
"""
"""
Importation des modules nécesaires pour le traitement de données
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://fbref.com/fr/comps/34/keepers/National-League-Stats")
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.findAll("div",class_= "overthrow table_container")
print(len(rows))

trs2 = rows[0].table.findAll("tr")
print(len(trs2))
trs2[0:][0].findAll("td",class_="right")[-1].text


