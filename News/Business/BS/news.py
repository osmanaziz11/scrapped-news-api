from bs4 import BeautifulSoup
import requests
from googletrans import Translator
# ================================
# Scrapped Business News from --- ---
#  need for translation
# ================================

baseURL="https://www.business-standard.com/category/international-news-economy-1160102.htm"
translater=Translator()
# Fetch HTML Content from the given link
def getHTMLContent():
   try:
       r = requests.get(baseURL)
       htmlContent = r.content
       soup = BeautifulSoup(htmlContent, "html.parser")
       return soup
   except:
       return 0

def getLinks():
    posts=[]
    soup=getHTMLContent()
    if soup != 0:
        mainDiv = soup.find("div", class_="listing-inner")
        contentDiv=mainDiv.findNext()
        for content in contentDiv.find_all("li"):
            title = content.find("h2")
            date = content.find("p")
            anchor = content.find("a")
            Link = anchor['href']
            thumbnail = anchor.find("img")['src']
            dict = \
                {
                    "title": "Not Available" if title == "None" else translater.translate(title.text,dest="ur").text,
                    "articleLink": Link,
                    "publishedAt": "Not available" if date == "None" else date.text,
                    "thumbnail": "Not available" if thumbnail == "None" else thumbnail,
                }

            posts.append(dict)

    return posts

def BusinessNews():
    return getLinks()
