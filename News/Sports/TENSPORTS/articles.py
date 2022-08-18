# =============================================
# extract article using slug
# base URL https://tensportstv.com/
# =============================================

from bs4 import BeautifulSoup
import requests

# ================================
# Scrapped Sports News Articles from TEN SPORTS
# ================================

baseURL="https://www.tensportstv.com/"

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
    article=""
    soup=getHTMLContent(slug)
    if soup != 0:
        mainDiv = soup.find("div", attrs={"data-td-block-uid":"tdi_75"})
        for para in mainDiv.find_all("p"):
            article += para.text + "\n"
    return article

def getArticles(slug):
    res=extractFromTheSource(slug)
    return res
