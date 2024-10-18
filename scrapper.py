import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Voir le code html source parse
print(soup)

#Voir le title de la page
print(soup.title.text)