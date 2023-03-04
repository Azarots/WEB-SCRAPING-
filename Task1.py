from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.15min.lt/"
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")

blokai = soup.find_all('div', class_="widget-horizontal-items swipeable")

galutinis = []

blokasv2 = blokai[0].find('div', class_='list-wrapper')
antrasciu_sarasas = list(blokasv2)

for i in range(1, len(antrasciu_sarasas)):
    try:
        antraste = antrasciu_sarasas[i].find("div", class_="item-info item-data").span
        try:
            if antraste["class"] == ["item-focus"]:
                galutinis.append(antraste.text + antraste.find_next("span").text)
        except:
            galutinis.append(antraste.text)
    except:
        pass

with open("15min_naujienos.csv", "w", encoding="UTF-8", newline="") as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(["Redakcija rekomenduoja: "])
    for j in galutinis:
        csv_writer.writerow([j])


