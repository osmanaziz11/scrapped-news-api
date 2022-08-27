
import News.Sports.BBC_URDU.News as SpNews
import News.Sports.BBC_URDU.articles as SpArticles

import News.Pakistan.BBC_URDU.news as PK_news
import News.Pakistan.BBC_URDU.article as PK_articles

import News.International.BBC_URDU.news as IntrNews
import News.International.BBC_URDU.article as IntrArticles

import News.Artist.BBC_URDU.news as Art
import News.Artist.BBC_URDU.article as ArtistArticle

import News.Business.BS.news as BNews
import News.Business.BS.article as BArticle

import News.Home.DuniyaNews.News as HNews
import News.Home.DuniyaNews.articles as HArticle

from flask import Flask,jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)
# Only Fetch Title, Thumbnail, Link to Main Article or Date
@app.route('/api/sports/news',methods=['GET'])
def main():
    resp=SpNews.SportsNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

#  Fetch Complete article from the source
@app.route('/api/sports/news/<slug>',methods=['POST'])
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
@app.route('/api/pakistan/news/<slug>',methods=['POST'])
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
@app.route('/api/international/news/<slug>',methods=['POST'])
def extractIntrArticles(slug):
    resp=IntrArticles.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})


# Fetch News for Artist from BBC URDU
@app.route('/api/artist/news',methods=['GET'])
def getArtistNews():
    resp=Art.ArtistNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})


# Fetch News for Business from ---
@app.route('/api/business/news',methods=['GET'])
def getBusinessNews():
    resp=BNews.BusinessNews()
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

# fetch articles
@app.route('/api/business/news/<slug>',methods=['GET'])
def extractBusinessArticle(slug):
    resp=BArticle.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})

# fetch articles
@app.route('/api/artist/news/<slug>',methods=['POST'])
def extractArtistArticles(slug):
    resp=ArtistArticle.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})

# Home
@app.route('/api/home/news')
def index():
    resp = HNews.HomeNews()
    if not resp:
        return jsonify({"message": "Not Ok", "status": 0, "posts": resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "posts": resp})

# fetch articles
@app.route('/api/home/news/<slug>',methods=['POST'])
def extractHomeArticle(slug):
    resp=HArticle.getArticles(slug)
    if not resp:
        return jsonify({"message":"Not Ok","status":0,"posts":resp})
    else:
        return jsonify({"message": "Ok", "status": 1, "description": resp})


# app.run(debug=True)


