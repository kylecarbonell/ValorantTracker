from mimetypes import init
from pickle import NONE
from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from discord import Embed
import json
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
        with open("Users.json") as f:
            self.file = json.load(f)

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

        pics = soup.find_all('image', href = True)
        if(len(pics) <= 0):
            self.pic = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.cults3d.com%2F4QqRV9kLYYEuw9ur_X3yjQl1sjk%3D%2F516x516%2Fhttps%3A%2F%2Ffiles.cults3d.com%2Fuploaders%2F15024335%2Fillustration-file%2Fa86d53e4-2bd9-4a8f-9550-986686c3131a%2Fgi0mAjIh_400x400.png&imgrefurl=https%3A%2F%2Fcults3d.com%2Fen%2F3d-model%2Fart%2Fvalorant-logo&tbnid=NtlHGJwaaD6E5M&vet=12ahUKEwiW3NTs_5P3AhWgHjQIHXYNDsUQMygDegUIARDEAQ..i&docid=PNy45xM50WJHYM&w=516&h=516&q=valorant%20logo&ved=2ahUKEwiW3NTs_5P3AhWgHjQIHXYNDsUQMygDegUIARDEAQ"
        else:
            self.pic = soup.find_all('image', href = True)[0]['href']
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
            return key + ": " + str(self.dict[key])
        else:
            return 'User Not Found!'

    def getAll(self, user):
        if(self.getUser(user) == False):
            return "No user found!"
        embed = Embed()
        embed.title = user.split("#")[0].capitalize() + " Stats"
        for i in self.dict:
            embed.add_field(name=i, value=self.dict[i], inline=False)

        embed.set_thumbnail(url=self.pic)

        return embed
    
    def connect(self, user, discord):
        for i in self.file:
            if(i['discordID'] == discord):
                return False
        self.file.append(
            {
                "valorantID": user,
                "discordID": discord
            }
        )

        with open("Users.json", 'w') as f:
            json.dump(self.file, f, indent=4, separators=(',', ':'))
        return True

    def getId(self, user):
        for i in self.file:
            if(i['discordID'] == user):
                return i['valorantID']

        return None