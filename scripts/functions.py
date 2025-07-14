# Imports
import requests
from bs4 import BeautifulSoup

#Scraping function

def scrape_data_indicators(url):

    response = requests.get(url)

    status_code = response.status_code #Se 200, ok
    latencia = response.elapsed.total #Tempo de resposta em segundos
    response_url = 1 if response.url == url else 0 #Url retornada é a url chamada

    return status_code, latencia, response_url






