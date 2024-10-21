import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Voir le code html source parse
#print(soup)

#Voir le title de la page
title_page = soup.title
text_h1 = soup.find("h1").text
print(soup.title.text)
print(title_page.text)

#Trouver et afficher les paragraphes ayant la class title
print(soup.find("p", class_="gem-c-document-list__item-description"))
print(soup.find_all("p", class_="gem-c-document-list__item-description"))
description_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []

for desc in description_bs:
    descriptions.append(desc.text)

print(descriptions)


#Trouver et afficher les listes prouits dans la page
list_products = soup.find_all('ul')
list_products_new = []

for product in list_products:
    list_products_new.append(product.text)

print(list_products_new)