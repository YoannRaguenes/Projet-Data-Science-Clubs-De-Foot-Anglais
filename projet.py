# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:20:21 2020

@author: Kévin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

##=== Renvoie le nombre de club qu'il y a eu au total dans le championnats anglais ===#
#alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z","oth"]
#res = []
#for carac in alphabet:
#    html = urlopen("http://fchd.info/index"+carac+".htm")
#    html_soup = BeautifulSoup(html, 'html.parser')
#    res = res + html_soup.findAll("li") 
##print(len(res))
    
#=== Renvoie le nombre d'équipe dans le championnat avec le classement/ le nom/ le meilleur buteur ===#
html = urlopen("https://fbref.com/fr/comps/34/National-League-Stats")
html_soup = BeautifulSoup(html, 'html.parser')
tab = html_soup.findAll("table", class_="min_width sortable stats_table", id ="results32361_overall")
#findAll renvoie une liste mais la on a qu'un élement d'ou le [0]
body = tab[0].findAll("tbody") 
rows = body[0].findAll("tr")
#print(len(rows))

teams = []
for row in rows:
    cells = row.findAll("td")
    cells2 = row.findAll("th")
    try:
        team_entry = {
                "classement": cells2[0].text,
                "Equipe": cells[0].text,
                "Meilleur buteur": cells[11].text,
                    }
        teams.append(team_entry)
    except ValueError:
            print("Ouch!")
df = pd.DataFrame(teams)

#print(df.head(24))
            

def without_but(entry):
    try:
        pos = entry.index("-")
        return str(entry[0:pos])
    except ValueError:
        return None
df["Meilleurs buteurs"] = df["Meilleur buteur"].apply(without_but)

#print(df.head(5))


def with_column_but(entry):
    try:
        pos = entry.index("-")
        return str(entry[pos+1:])#deux point jusqu'a la fin
    except ValueError:
        return None
df["Nombre de but"] = df["Meilleur buteur"].apply(with_column_but)



del df["Meilleur buteur"]#elle est en trop car je l'ai rename
#print(df.head(3))

df.to_csv("teams.csv", sep=",")

craftcans = pd.read_csv("teams.csv", sep=",", encoding="latin1")
print(craftcans.head(5))
print(df.head(3))








