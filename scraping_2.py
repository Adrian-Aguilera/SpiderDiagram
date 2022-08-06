import re
from unittest import result
from bs4 import BeautifulSoup
import requests

pagina = requests.get("https://10ejemplos.com/")
soup = BeautifulSoup(pagina.text, "html.parser")
tags = soup('a')

for tag in tags:
   test = tag.get('href')

diccionario = {}

datos = {'links':tag.get('href')}

print (datos)