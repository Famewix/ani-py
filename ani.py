from pydoc import text
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

    def take_input(self, text, min, max, i_type=int):
        while True:
            try:
                result = i_type(input(text))
                if result < min:
                    print("Value too small.")
                elif result > max:
                    print("Value too big.")
                else:
                    break
            except ValueError:
                print("Invalid Input")
        return result



    def search(self, keyword):
        r = requests.get(f"{self.BASE_URL}/search.html?keyword={keyword}")
        bs = BeautifulSoup(r.text, 'html.parser')
        names = bs.find_all('p', attrs={'class': "name"})

        for index, name in enumerate(names):
            title = name.a['title']
            print(self.numbering(index), title)

        anime_number = self.take_input(text="Enter Anime Index: ", min=0, max=len(names))
        anime_title = names[anime_number].a['title']
        anime_url = urlparse.urljoin(self.BASE_URL, names[anime_number].a['href'])
        self.select_anime(anime_title, anime_url)

    def select_anime(self, anime_title, anime_url):
        r = requests.get(anime_url)
        bs = BeautifulSoup(r.text, "html.parser")
        ep_count = bs.find("ul", attrs={'id':"episode_page"}).li.a.text
        episodes = bs.find('div', attrs={"class":"anime_video_body"})
        # ep_number = self.take_input(text="Enter Anime Index: ", min=0, max=len(names))
        print(episodes)

def main():
    ani_py = AniPy()
    # ani_py.search("attack")
    ani_py.select_anime("Ashita e Attack!", "https://www1.gogoanime.pe/category/ashita-e-attack")

if __name__ == "__main__":
    main()
