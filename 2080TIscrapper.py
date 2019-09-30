from bs4 import BeautifulSoup
import requests

filename = "products2080TI.csv"
f = open(filename, 'w')

headers = 'Product name, Image, Price, Stock, Description\n'

f.write(headers)

response = requests.get("https://www.pccasegear.com/category/193_1966/graphics-cards/geforce-rtx-2080-ti")  # insert custom site
soup = BeautifulSoup(response.text, 'html.parser')

containers = soup.findAll('li', {"class": "media m-t-10"})

for container in containers:
    name = container.div.div.img["title"].strip()
    image = container.div.div.img["src"]

    desc = container.p.text.strip()
    button_object = container.find('div', {"class": "btn-for-mobile price-btn"})
    price = button_object.h2.text.replace('$', '')
    stock = button_object.span.text.strip()

    print(name)
    print(image)
    print(desc)
    print(price)
    print(stock)
    print()

    f.write(name + ',' + image + ',' + price + ',' + stock + ',' + desc.replace(',', '|') + "\n")

f.close()





