from mimetypes import init
from pickle import NONE
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Functions:
    def __init__(self):
        #Dictionary
        self.dict = {
            "K/D Ratio" : 0,
            "Headshots" : 0,
            "Wins" : 0,
            "Kills" : 0,
            "Aces" : 0,
            "Most Kills (Match)" : 0
        }

    def getUser(self):
        #Request Player
        user = input("Username and ID: ")

        #Create needed objects
        path = Service('C:\Program Files (x86)\chromedriver.exe')
        browser = webdriver.Chrome(service=path)
        url = 'https://tracker.gg/valorant'
        browser.get(url)

        #Search Bar
        search = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input')
        search.send_keys(user)
        search.send_keys(Keys.RETURN)
        time.sleep(3)

        text = browser.page_source
        browser.quit()

        #HTML Parser
        soup = BeautifulSoup(text, "html.parser")
        stats = soup.find_all('div', class_ = 'numbers')
        
        #Print stats
        for stat in stats:
            numbers = stat.find('span', class_="value").text
            titles = stat.find('span', class_="name").text
            for i in self.dict:
                if i == titles:
                    self.dict[i] = numbers

    def getStat(self, key):
        return key + ": " + self.dict[key]



#Bot: /kd dazaichann
#self.dict["K/D Ratio"] = your KD
