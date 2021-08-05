from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_source,get_articles
from ..models import NewsSource

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index page and its data
	'''
	technology = get_news_source('technology')
	business = get_news_source('business')
	sports = get_news_source('sports')
	entertainment = get_news_source('entertainment')
	title = "News Room"

	return render_template('index.html',title = title, technology = technology,business = business,sports = sports,entertainment = entertainment)



@main.route('/news_articles/<id>')
def articles(id):
	'''
	view articles  page function that returns the articles page and its data
	'''
	articles = get_articles(id)
	title = f'News Room articles | {id}'

	return render_template('news_articles.html',title= title,articles = articles)
