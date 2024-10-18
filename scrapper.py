import requests

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

# Voir le code html source
print(page.content)