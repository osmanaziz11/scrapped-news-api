# =============================================
# extract article using slug
# base URL https://www.bbc.com/urdu/
# =============================================

from bs4 import BeautifulSoup
import requests


baseURL="https://www.bbc.com/urdu/"

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
        mainDiv = soup.find("main", attrs={"role":"main"})
        title=mainDiv.find("h1",{"id":"content"})
        timeDiv=mainDiv.find("div",class_="e1j2237y7")

        time=timeDiv.findNext() if timeDiv != None else None
        for figure in mainDiv.find_all("div",class_="bbc-1pt3yso"):
           images.append(figure.find("img")['src'])

        for para in mainDiv.find_all("p",class_="bbc-yabuuk"):
            if para.text:
                article += para.text + "\n"
        dict = \
            {
                "title": "Not Available" if title == None else title.text,
                "publishedAt": "Not available" if time == None else time.text,
                "thumbnail": images,
                "article":article,
            }
    return dict

def getArticles(slug):
    res=extractFromTheSource(slug)
    return res
