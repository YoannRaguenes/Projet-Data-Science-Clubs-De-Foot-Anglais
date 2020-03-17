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

"""
Récupération des données du premier tableu présent sur la page
"""
html = urlopen("https://fbref.com/fr/comps/34/keepers/National-League-Stats")
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.findAll("tr")
print(rows)


l=[]
for row in rows:
    head = row.findAll("td", class_="right")
    equipe = row.findAll("th", scope="row")
    if len(head) == 18:
        try:
            if equipe != []:
                equipe=equipe[0].text
            head_entry ={
                    "Equipe": equipe,
                    "JC" : head[0].text,
                    "Titulaire" : head[2].text
                    }
            l.append(head_entry)
        except ValueError:
            print("Ouch!")

print(l)


df = pd.DataFrame(l)
df.to_csv("gardiens.csv")



"""
Tentative de récupération des données du 2 ème tableau
"""
html = urlopen("https://fbref.com/fr/comps/34/keepers/National-League-Stats")
html_soup = BeautifulSoup(html, 'html.parser')
bodys= html_soup.findAll("body")

for body in bodys:    
    divs=body.findAll("div", role="main")  
    for div in divs:
        divs2=div.findAll("div") #<div class="table_outer_container"> est impossible d'accès (impossible de la trouver dans les divs)
        for div2 in divs2:
            trs=div2.findAll("div")
            print("bal")
            print(trs)








