# =============================================
# extract article using slug
# base URL https://www.bbc.com/urdu/
# =============================================

from bs4 import BeautifulSoup
import requests
from googletrans import Translator

baseURL="https://www.business-standard.com/article/international/"
translater=Translator()
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
    article=""
    soup=getHTMLContent(slug)
    if soup != 0:
        mainDiv=soup.find("div",class_="main-cont-left")
        mainTitle = mainDiv.find("div", class_="pB0").findNext()

        published=mainDiv.find("span",attrs={"itemprop":"datePublished"})

        thumbnail=mainDiv.find("div",class_="colL_MktColumn0").find("img",class_="imgCont")['src']

        mainPara=mainDiv.find("span",class_="p-content")

        for para in mainPara.find_all("p"):
            if para.text:
                article += para.text + "\n"
        dict = \
            {
                "title": "Not Available" if mainTitle == "None" else translater.translate(mainTitle.text,dest="ur").text,
                "publishedAt": "Not available" if published == "None" else translater.translate(published.text,dest="ur").text,
                "thumbnail": thumbnail,
                "article":translater.translate(article,dest="ur").text,
            }
        print(dict)
    return dict

def getArticles(slug):
    res=extractFromTheSource(slug)
    return res
