import requests
from bs4 import BeautifulSoup
import urllib

load_irl = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_irl)
soup = BeautifulSoup(html.content, "html.parser")

for element in soup.find_all("a"):
    print(element.text)
    url=element.get("href")
    link_url=urllib.parse.urljoin(load_irl,url)
    print(link_url)