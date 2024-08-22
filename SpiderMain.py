import requests
from bs4 import BeautifulSoup

def downloadIMG(url):
    r = requests.get(url).content
    with open('img.jpg', 'wb+') as i:
        i.write(r)


if __name__ == "__main__":
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
        imgUrl = img.get('src')
        downloadIMG(imgUrl)

