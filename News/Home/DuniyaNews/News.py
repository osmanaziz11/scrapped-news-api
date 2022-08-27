from bs4 import BeautifulSoup
import requests

# ================================
# Scrapped Home News from Duniya News
# No need for translation
# ================================

baseURL="https://urdu.dunyanews.tv/index.php/en/World"

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
        mainDiv = soup.find("div", class_="impcatg")
        sliderContent=mainDiv.find("div",class_="newsBox")
        for row in sliderContent.find_all("div",class_="row"):
            title=row.find("h3").findNext()
            thumbnail=row.find('img')['src']
            publishedAt=row.find("div",class_="newsdate")
            articleLink=row.find("a")['href']
            dict = \
                {
                    "title": "Not Available" if title == None else title.text,
                    "articleLink": articleLink,
                    "publishedAt": "Not available" if publishedAt == None else publishedAt.text,
                    "thumbnail": "Not available" if thumbnail == None else thumbnail,
                }
            posts.append(dict)
        news = soup.find("div", class_="categories")
        # print(news)
        for item in news.find_all("div",class_="cNewsBox"):
            anchor=item.find("a")
            articleLink=anchor['href']
            thumbnail=anchor.findNext()['src']
            title = item.find("h3").findNext()
            shortDesc=item.find("p")
            publishedAt = item.find("div", class_="newsdate")
            dict = \
                {
                    "title": "Not Available" if title == None else title.text,
                    "articleLink": articleLink,
                    "publishedAt": "Not available" if publishedAt == None else publishedAt.text,
                    "thumbnail": "Not available" if thumbnail == None else thumbnail,
                    "shortDesc":"Not available" if shortDesc == None else shortDesc.text
                }
            posts.append(dict)
        return posts
    return 0
def HomeNews():
    return getLinks()
