import random
import requests # pip install requests
from bs4 import BeautifulSoup # pip install  bs4

url = 'https://www.imdb.com/chart/top'

if __name__ == '__main__':
    main()

def main():
    response = requests.get(url)
    html = response.text 