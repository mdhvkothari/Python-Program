from django.shortcuts import render
import json
import requests
from django.http import HttpResponse

def home(request):
    api_request = requests.get("https://newsapi.org/v2/sources?country=in&apiKey=24bcccedf20d412aa67dc9693f58d729")

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error"
    data = api['sources']
    return render(request,'home.html',{'data':data})

def about(request):
    return render(request,'about.html')

def article(request,url):
    api_request_article = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=24bcccedf20d412aa67dc9693f58d729")
    try:
        api_article = json.loads(api_request_article.content)
    except Exception as e:
        api_article ="Error"
    data_article = api_article['articles']
    return render(request,'article.html')
