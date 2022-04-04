from bs4 import BeautifulSoup
import requests

text = requests.get('https://tracker.gg/valorant/profile/riot/SEN%20TenZ%230505/overview').text
soup = BeautifulSoup(text, "html.parser")

stats = soup.find_all('div', class_ = 'numbers')

#K/D Stat
numbers = stats[1].find('span', class_="value").text
print(f"K/D Ratio: {numbers}")
# kd = stats.find_all('')


