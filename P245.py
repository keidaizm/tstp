import os
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    siteinfo = []

    def __init__(self,site):
        self.site = site

        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open("data.txt", "w") as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if "html" in url:
                    print("\n" + url)
                    f.write(url + "\n")

news = "https://www.zmp.co.jp/"
Scraper(news).scrape()

"""saving the scraiping data"""
#st = open("data.txt", "w")
#st.write(d)
#st.close()

        

"""
a = 'https://news.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja'
b = Scraper(a).scrape()
print(b)
"""



