# =============================================
# extract article using slug
# =============================================

from bs4 import BeautifulSoup
import requests


baseURL="https://urdu.dunyanews.tv/index.php/ur/World/"

# Fetch HTML Content from the given link
def getHTMLContent(slug):
   try:
       r = requests.get(baseURL+slug+"/")
       htmlContent = r.content
       soup = BeautifulSoup(htmlContent, "html.parser")
       return soup
   except:
       return 0

def extractFromTheSource(slug):
    dict={}
    images=[]
    article=""
    soup=getHTMLContent(slug)
    if soup != 0:
        mainDiv = soup.find("div", class_="news-content")
        title=mainDiv.findNext()
        row=mainDiv.find("div",class_="row")
        timeDiv=row.find("div",class_="newsdate")
        time=timeDiv.findNext() if timeDiv != None else None
        thumbnail=mainDiv.find("img")['src']
        images.append(thumbnail)
        paraDiv=mainDiv.find("div",class_="main-news")

        for para in paraDiv.find_all("p"):
            if para.text:
                article += para.text + "\n"
        dict = \
            {
                "title": "Not Available" if title == None else title.text,
                "publishedAt": "Not available" if time == None else time.text,
                "thumbnail": images,
                "article":article,
            }
        print(dict)
    return dict

def getArticles(slug):
    res=extractFromTheSource(slug)
    return res
