import requests
from bs4 import BeautifulSoup
import re
import csv


def rast_visus_telefonus_puslapyje(puslapiu_kiekis):
    bloku_sarasas = []
    if puslapiu_kiekis == 1:
        url = 'https://www.telia.lt/prekes/mobilieji-telefonai?q=%3Arelevance&page=1'
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'html.parser')
        bloku_sarasas.append(soup.find_all('div',
                                           class_="mobiles-product-card card card__product card--anim js-product-compare-product"))
    else:
        for puslapis in range(1, puslapiu_kiekis + 1):
            url = f'https://www.telia.lt/prekes/mobilieji-telefonai?q=%3Arelevance&page={puslapis}'
            source = requests.get(url)
            soup = BeautifulSoup(source.text, 'html.parser')
            bloku_sarasas.append(soup.find_all('div',
                                               class_="mobiles-product-card card card__product card--anim js-product-compare-product"))
    return bloku_sarasas


def rasti_telefonus_ir_kainas(blokai):
    with open("Telefonai.csv", "w", encoding="UTF-8", newline="") as failas:
        kainu_zodynas = {}
        csv_writer = csv.writer(failas)
        csv_writer.writerow(['Telefono pavadinimas', 'Kaina'])
        for j in blokai:
            for i in range(len(j)):
                try:
                    pavadinimas = j[i].find('a', class_='mobiles-product-card__title js-open-product').text.strip()
                    kaina = j[i].find('div', attrs={'class': 'mobiles-product-card__full-price price'}).div.text.strip()
                    kaina_filtruota = re.sub('[^0-9]', '', kaina)
                    kainu_zodynas[pavadinimas] = int(kaina_filtruota)
                except:
                    pass
        for k, v in kainu_zodynas.items():
            csv_writer.writerow([k] + [v])
    return f'Brangiausias telefonas - {max(kainu_zodynas, key=kainu_zodynas.get)} ir jis kainuoja {max(kainu_zodynas.values())}€\n' \
           f'Pigiausias telefonas - {min(kainu_zodynas, key=kainu_zodynas.get)} ir jis kainuoja {min(kainu_zodynas.values())}€'
