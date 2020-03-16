from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd




html = urlopen("https://fbref.com/fr/players/3071a619/Nolan-Roux")
html_soup = BeautifulSoup(html, 'html.parser')
infos = html_soup.findAll('span')  #8eme



    
#print(len(infos))
for i in range(6,11,1):
    date=infos[i].text
    chaine=date[-9:]
    if chaine[:2]=='19' or chaine[:2]=='20':
        print(date[-9:]) 
        
        
#date=infos[10].text
#date=str(date)
#       
#print(date[-9:])  


#nb = 0
#date=[]
#for info in infos:
#    cells = info.findAll("data-birth")
#    date
#print(nb)