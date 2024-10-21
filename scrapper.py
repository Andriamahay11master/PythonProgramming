import requests
import csv
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
titles = soup.find_all("a", class_="govuk-link")
titres = []

for title in titles:
    titres.append(title.text)

print('titres',titres)

#Trouver et afficher les paragraphes ayant la class title
#print(soup.find("p", class_="gem-c-document-list__item-description"))
#print(soup.find_all("p", class_="gem-c-document-list__item-description"))
description_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []

for desc in description_bs:
    descriptions.append(desc.text)

print('desc',descriptions)

# Créer une liste pour les en-têtes
en_tete = ["titre", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
    for titre, description in zip(titres, descriptions):
        # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
        ligne = [titre, description]
        writer.writerow(ligne)
