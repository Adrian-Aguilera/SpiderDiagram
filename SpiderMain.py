import requests
from bs4 import BeautifulSoup

# URL
url = 'https://www.superselectos.com/'
response = requests.get(url)

#parcer el contenido de la pagina a texto
soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')
print("\nEnlaces:")
for link in links:
    print(link.get('href'))

# Extraer y mostrar todas las imagenes
images = soup.find_all('img')
print("\nImágenes:")
for img in images:
    print(img.get('src'))
