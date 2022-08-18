from bs4 import BeautifulSoup
import requests

# ================================
# Scrapped Pakistan News from BBC URDU
# No need for translation
# ================================

baseURL="https://www.bbc.com/urdu/topics/cjgn7n9zzq7t"

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
        mainDiv = soup.find("ul", class_="bbc-1kz5jpr")
        for content in mainDiv.find_all("li", class_="bbc-n8va9n"):
            title = content.find("h2")
            anchor = title.findNext()

            Link = anchor['href']
            date = content.find("time")
            thumbnail = content.find("img")['src']

            dict = \
                {
                    "title": "Not Available" if anchor == "None" else anchor.text,
                    "articleLink": Link,
                    "publishedAt": "Not available" if date == "None" else date.text,
                    "thumbnail": "Not available" if thumbnail == "None" else thumbnail,
                }
            posts.append(dict)

    return posts

def PakistanNews():
    return getLinks()
