from typing import KeysView
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

#Create needed objects
browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
url = 'https://tracker.gg/valorant'
browser.get(url)
text = requests.get(url).text

#HTML Parser
soup = BeautifulSoup(text, "html.parser")

#Search bar
searchBar = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/form')
searchBar.send_keys("Tenz")
searchBar.send_keys(Keys.RETURN)


stats = soup.find_all('div', class_ = 'numbers')

#Selenium: Find person


#Print stats
for stat in stats:
    numbers = stat.find('span', class_="value").text
    titles = stat.find('span', class_="name").text
    print(f"{titles}: {numbers}")
    print('')
# kd = stats.find_all('')


