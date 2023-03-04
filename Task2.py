from bs4 import BeautifulSoup
import requests

url = "https://www.delfi.lt/"

source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")

headlines = soup.find_all('h3', class_='headline-title')

count_headlines = 0

for headline in headlines:
    count_headlines += 1

print(f"Todays Delfi.lt website has: {count_headlines}, headlines")
