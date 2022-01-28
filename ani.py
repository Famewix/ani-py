import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import urllib.parse as urlparse

init(autoreset=True)


class AniPy:
    def __init__(self):
        self.BASE_URL = "https://www1.gogoanime.pe/"

    def numbering(self, num):
        return f"{Fore.CYAN}[{Fore.WHITE}{num}{Fore.CYAN}]"

    def search(self, keyword):
        r = requests.get(f"{self.BASE_URL}/search.html?keyword={keyword}")
        bs = BeautifulSoup(r.text, 'html.parser')
        names = bs.find_all('p', attrs={'class': "name"})


        for index, name in enumerate(names):
            title = name.a['title']
            print(self.numbering(index), title)

        anime_number = int(input("Enter Anime Index: "))
        anime_title = names[anime_number].a['title']
        anime_url = urlparse.urljoin(self.BASE_URL, names[anime_number].a['href'])
        print(anime_title)
        print(anime_url)

def main():
    ani_py = AniPy()
    ani_py.search("attack")

if __name__ == "__main__":
    main()
