
import News.Sports.TENSPORTS.News as SpNews
import News.Sports.TENSPORTS.articles as SpArticles

import News.Pakistan.BBC_URDU.news as PK_news
import News.Pakistan.BBC_URDU.article as PK_articles

import News.International.BBC_URDU.news as IntrNews
import News.International.BBC_URDU.article as IntrArticles

import News.Artist.BBC_URDU.news as ArtistNews
import News.Artist.BBC_URDU.article as ArtistArticle

from flask import Flask,jsonify

app = Flask(__name__)

# Only Fetch Title, Thumbnail, Link to Main Article or Date
@app.route('/api/sports/news',methods=['GET'])
def main():
    resp=SpNews.SportsNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

#  Fetch Complete article from the source
@app.route('/api/sports/news/<slug>',methods=['GET'])
def extractArticle(slug):
    resp=SpArticles.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})


# Fetch News for PAKISTAN from BBC URDU
@app.route('/api/pakistan/news',methods=['GET'])
def getPKNews():
    resp=PK_news.PakistanNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

# fetch articles
@app.route('/api/pakistan/news/<slug>',methods=['GET'])
def extractPkArticle(slug):
    resp=PK_articles.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})


# Fetch News for International from BBC URDU
@app.route('/api/international/news',methods=['GET'])
def getIntrNews():
    resp=IntrNews.InternationalNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

# fetch articles
@app.route('/api/international/news/<slug>',methods=['GET'])
def extractIntrArticles(slug):
    resp=IntrArticles.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})


# Fetch News for Artist from BBC URDU
@app.route('/api/artist/news',methods=['GET'])
def getArtistNews():
    resp=ArtistNews.ArtistNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

# fetch articles
@app.route('/api/artist/news/<slug>',methods=['GET'])
def extractArtistArticles(slug):
    resp=ArtistArticle.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})

@app.route('/')
def index():
   return "REST API"





