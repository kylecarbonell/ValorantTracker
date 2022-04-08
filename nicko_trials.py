from mimetypes import init
from pickle import NONE
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import hikari
import lightbulb

def getStat(user,key):

    dict = {
    "K/D Ratio" : 0,
    "Headshots" : 0,
    "Wins" : 0,
    "Kills" : 0,
    "Aces" : 0,
    "Most Kills (Match)" : 0
    }

    #define browser and url
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
    
    #Edit dictionary with correct values
    for stat in stats:
        numbers = stat.find('span', class_="value").text
        titles = stat.find('span', class_="name").text
        for i in dict:
            if i == titles:
                dict[i] = numbers

    #return the desired value for the desired user
    return key + ": " + dict[key]

#define bot
bot = lightbulb.BotApp(token='OTYxODg5OTk5NzM1ODgxNzU4.Yk_j3g.nuH6kgXlXm4iProHqhhHdkAJGco')

@bot.command
@lightbulb.command('kd', 'Input a valid Valorant username and id')
@lightbulb.implements(lightbulb.SlashCommand)
async def kd(ctx, user):
    await ctx.respond(getStat(user, "K/D Ratio"))

bot.run()