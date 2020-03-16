# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 08:16:09 2020

@author: Kévin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
#The site changed, this URL is no longer valid
#html = urlopen("http://craftcans.com/db.php?search=all&sort=beerid&ord=desc&view=text")

#Please use:
html = urlopen("https://web.archive.org/web/20150929001305/http://craftcans.com/db.php?search=all&view=text")
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.findAll("tr")
print(len(rows))



nb = 0
for row in rows:
    cells = row.findAll("td")
    if (len(cells) == 8):   
         nb = nb + 1
print(nb)


nb = 0
for row in rows:
    cells = row.findAll("td")
    if (len(cells)==8):
        id = cells[0].text
        id = id[0:len(id)-1]
        try:
            id = int(id)
            nb = nb + 1
        except ValueError:
            print("Ouch!")
print(nb)


beers = []
for row in rows:
    cells = row.findAll("td")
    if (len(cells) == 8):
        id = cells[0].text
        id = id[0:len(id)-1]
        try:
            id = int(id)
            beer_entry = {
                    "id": id,
                    "name": cells[1].text,
                    "brewery_name": cells[2].text,
                    "brewery_location": cells[3].text,
                    "style": cells[4].text,
                    "size": cells[5].text,
                    "abv": cells[6].text,
                    "ibu": cells[7].text
                    }
            beers.append(beer_entry)
        except ValueError:
            print("Ouch!")

df = pd.DataFrame(beers)

print(df.head(5))


units = df["size"]
units = list(set(units))
print(units)

unique_unit = []
for unit in units:
    try:
        value = float(unit)
        unique_unit.append(value)
    except ValueError:
        pos = unit.index(" ")
        unique_unit.append(unit[0:pos])
print(list(set(unique_unit)))



def without_ounces(entry):
    try:
        return float(entry)
    except ValueError:
        pos = entry.index(" ")
        return float(entry[0:pos])

df["volume"] = df["size"].apply(without_ounces)
print(df.head(5))

del df["size"]
print(df.head(5))


nb = 0
abvs = df["abv"]
for abv in abvs:
    if ('%' in abv):
        nb = nb + 1
print(nb)

def without_percent(entry):
    entry = entry.strip("%")
    try:
        return float(entry)
    except ValueError:
        return None
df["abv"] = df["abv"].apply(without_percent)
print(df.head(5))

def to_int(entry):
    try:
        return int(entry)
    except ValueError:
        return None
df["ibu"] = df["ibu"].apply(to_int)
print(df.head(5))

df.to_csv("beers.csv", sep=' ')

craftcans = pd.read_csv("beers.csv", sep=' ', encoding="latin1")
print(craftcans.head(5))
craftcans.columns = ["id", "abv", "location", "name", "ibu", "beer_id", "name", "style", "volume"]
print(craftcans.head(5))


