from bs4 import BeautifulSoup
import requests
import csv
import re

phones = []

for i in range(0, 5):
    url = f"https://www.telia.lt/prekes/mobilieji-telefonai?q=%3Arelevance&page={i}"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    order_list = soup.find_all("div",
                               class_="mobiles-product-card card card__product card--anim js-product-compare-product")

    for order in order_list:
        phone_titles = order.find("a", class_="mobiles-product-card__title js-open-product").text.strip()
        price = order.find('div', class_='mobiles-product-card__full-price price').div.text.strip()
        price_filer = re.sub('[^0-9]', '', price)
        phones.append([phone_titles, price_filer + "€"])

with open("phones.csv", "w", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Phone Title", " Price"])
    for phone in phones:
        writer.writerow(phone)


phones_with_prices = []
for phone in phones:
    phone_title = phone[0]
    price = int(phone[1].replace("€", ""))
    phones_with_prices.append([phone_title, price])


most_expensive_phone = max(phones_with_prices, key=lambda x: x[1])
lowest_price_phone = min(phones_with_prices, key=lambda x: x[1])

print(f"Most expensive phone:, {most_expensive_phone[0]} {most_expensive_phone[1]} ")
print(f"Lowest price phone: {lowest_price_phone[0]} {lowest_price_phone[1]} €")

