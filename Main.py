from bs4 import BeautifulSoup
import requests

text = requests.get('https://tracker.gg/valorant/profile/riot/SEN%20TenZ%230505/overview').text
soup = BeautifulSoup(text, "html.parser")

stats = soup.find_all('div', class_ = 'numbers')

#K/D Stat


for stat in stats:
    numbers = stat.find('span', class_="value").text
    titles = stat.find('span', class_="name").text
    print(f"{titles}: {numbers}")
    print('')
# kd = stats.find_all('')


