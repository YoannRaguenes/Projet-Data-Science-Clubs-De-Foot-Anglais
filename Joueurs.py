# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:16:11 2020

@author: Kévin
"""

from selenium import webdriver
import urllib
#The URL to search on Google
url = "https://fbref.com/fr/comps/34/stats/National-League-Stats"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome("/Users/Kévin/Downloads/chromedriver_win32/chromedriver")
#Open the page on Chrome
browser.get(url)
#Use for site robot
header={'User-Agent':" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
elt = browser.find_elements_by_xpath('//div[contains(@class,"table_outer_container")]')
elt = elt[1].find_element_by_tag_name("table")
elt.find_element_by_tag_name("tbody")
elt.find_element_by_tag_name("tbody").text
players = elt.find_elements_by_tag_name("tr")


for play in players:
    if play =="Clt Joueur":
        players.remove(play)
    print(play.text)
    
