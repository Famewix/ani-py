import requests
from bs4 import BeautifulSoup


class AniPy:
    def __init__(self) -> None:
        self.BASE_URL = "https://www1.gogoanime.pe/"

    def search(self, keyword):
        r = requests.get(f"{self.BASE_URL}/search.html?keyword={keyword}")
        bs = BeautifulSoup(r.text, 'html.parser')
        names = bs.find_all('p', attrs={'class': "name"})

        for name in names:
            print(name.a['title'])

def main():
    ani_py = AniPy()
    ani_py.search("attack")

if __name__ == "__main__":
    main()
