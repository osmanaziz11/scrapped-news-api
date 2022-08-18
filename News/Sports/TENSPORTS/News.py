from bs4 import BeautifulSoup
import requests

# ================================
# Scrapped Sports News from TEN SPORTS
# ================================

mainURL="https://www.tensportstv.com/category/news/"
links=[]

# Fetch HTML Content from the given link
def getHTMLContent():
   try:
       r = requests.get(mainURL)
       htmlContent = r.content
       soup = BeautifulSoup(htmlContent, "html.parser")
       return soup
   except:
       return 0

def getLinks():
    posts=[]
    soup=getHTMLContent()
    if soup != 0:
        mainDiv = soup.find("div", {"id": "tdi_59"})
        for content in mainDiv.find_all("div", class_="tdb_module_loop"):
            para = content.find("p", class_="entry-title")
            anchor = para.findNext()

            Link = anchor['href']
            date = content.find("time", class_="entry-date")
            thumbnail = content.find("span", class_="entry-thumb")['style'][22:-1]

            dict = \
                {
                    "title": "Not Available" if anchor == "None" else anchor.text,
                    "articleLink": Link,
                    "publishedAt": "Not available" if date == "None" else date.text,
                    "thumbnail": "Not available" if thumbnail == "None" else thumbnail,
                }
            posts.append(dict)

    return posts

def SportsNews():
    return getLinks()
