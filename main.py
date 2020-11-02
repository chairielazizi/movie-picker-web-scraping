import random
import requests # pip install requests
from bs4 import BeautifulSoup # pip install  bs4

url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')


    movietag0 = movietags[0]
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        # print(moviesplit)
        return year

    years = [get_year(tag) for tag in movietags]

    innermovietag0 = inner_movietags[0]
    print(innermovietag0)
    # print(movietag0)

    

if __name__ == '__main__':
    main()