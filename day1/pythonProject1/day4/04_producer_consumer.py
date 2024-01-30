from urllib.request import urlopen
from bs4 import BeautifulSoup
import multiprocessing.dummy as mp
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

q = mp.Queue()


def process(url) -> tuple[str, list[str]]:
    with urlopen(url, context=ctx) as response:
        text = response.read()
        soup = BeautifulSoup(text, features="html.parser")
        title = soup.find("title").text
        links = [
            "https://docs.python.org/3/library/" + a["href"]
            for a in soup.find_all("a")
            if re.match(r"^[a-z]+\.html$", a["href"])
        ]
        return (title, links)


def runner():
    while True:
        link = q.get()
        title, new_links = process(link)
        print(title)
        for link in new_links:
            q.put(link)


"""
Exercise:
1. Don't process twice the same link
2. Use multiple processes to speed up the program
"""

if __name__ == "__main__":
    q.put("https://docs.python.org/3/library/index.html")
    runner()