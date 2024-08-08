import requests
import time
from bs4 import BeautifulSoup
import validators

#list the site to those who don't search
def is_blacklist(links):
        list = ["facebook", "twitter","google","apple", "youtube"]
        for i in list:
                if  i in links:
                        return True
        return False

#main fuction
def urls(url,current_level):
        pagina = requests.get(url)
        sopa = BeautifulSoup(pagina.content, 'html.parser')
        for link in sopa.find_all('a'):
                links = (link.get('href'))
                if (links is not None):
                    if not is_blacklist(links):
                        if (links not in visitados and validators.url(links)):
                                visitados.append(links)
                                print(("|") * current_level, current_level, ">" , links)
                                #time.sleep(0.01)
                                urls(links, current_level + 1)


if __name__ == "__main__":
    site = input("your site: ")
    init_url = f"{site}"
    redes= []
    level = 0
    visitados = []
    urls(init_url, level)