from mimetypes import init
from pickle import NONE
from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from discord import Embed
import time

class Functions:
    def __init__(self):
        #Dictionary for player stats
        self.dict = {
            "K/D Ratio" : 0,
            "Headshots" : 0,
            "Wins" : 0,
            "Kills" : 0,
            "Aces" : 0,
            "Most Kills (Match)" : 0
        }

        self.pic = ""

    def getUser(self, user):
        if('#' in user == False):
            return False

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

        #Saves browser source code
        text = browser.page_source
        browser.quit()

        #HTML Parser
        soup = BeautifulSoup(text, "html.parser")

        #Check if USER Exists
        check = soup.find_all('div', class_ = 'content content--error')
        if(len(check) != 0):
            return False

        #Puts stats into a dictionary
        stats = soup.find_all('div', class_ = 'numbers')
        self.pic = soup.find_all('image', href = True)[0]
        print(self.pic)
        for stat in stats:
            numbers = stat.find('span', class_="value").text
            titles = stat.find('span', class_="name").text
            for i in self.dict:
                if i == titles:
                    self.dict[i] = numbers

        return True

    def getStat(self, key, user):
        #Gets stat based on dictionary key
        if(self.getUser(user)):
            return key + ": " + self.dict[key]
        else:
            return 'User Not Found!'

    def getAll(self, user):
        self.getUser(user)
        embed = Embed()
        embed.title = user.split("#")[0].capitalize() + " Stats"
        for i in self.dict:
            embed.add_field(name=i, value=self.dict[i], inline=True)

        embed.thumbnail = self.pic

        return embed