from bs4 import BeautifulSoup
import requests

SITE = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(SITE, 'html.parser')

temperatura = soup.find("span", class_="temperature _margin-l-5 -font-13")

print(temperatura.string)

