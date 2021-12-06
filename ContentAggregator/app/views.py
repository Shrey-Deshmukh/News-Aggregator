from app.models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse
import feedparser
import requests
from bs4 import BeautifulSoup
import re
import urllib

# Create your views here.
def updatepython(request):
   
    #-------python----------------
   # url = feedparser.parse("https://medium.com/feed/tag/python" )

    toi_r = requests.get("https://www.thehindu.com/")
    toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

    toi_headings = toi_soup.find_all('div', {'class':'story-card'})
    
    
    news_title = []
    news_url = []
    news_images = []
  
    for article in toi_headings:
       
            main1 = article.find_all('a')[0]    
            main1 = str(main1)
            link = re.findall(r'href=\"(.*?)\"', main1)
            imagelink = article.find_all('img')[0]
            imagelink = str(imagelink)
            image = re.findall(r'data-src-template=\"(.*?)\"', main1)
    
            title = article.find_all('h2')
    
            title = str(title)

            title1 = title.split("\n")
        
            if len(title1) != 1:
               news_title.append(title1[2])
               
               link = str(link)
               news_url.append(link[2:-2])
               
               image = str(image)
               news_images.append(image[2:-2])
              
             
            
        
    
    for i in range(len(news_url)):
         content= PyContent()
         content.headline = str(news_title[i])
         content.url = str(news_url[i])
         content.img = str(news_images[i])
         content.save()
    return redirect('/')

def updatecovid(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/covid"
        )
    for i in range(10):
        info = url.entries[i]
        content= CovidContent()
        content.headline= info.title
        print("################################")
        print(content.headline)
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)

        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')

def updateprog(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )
    for i in range(10):
        info = url.entries[i]
        content= ProgContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)

        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')

def updatehiring(request):
    #-------python----------------
    url = feedparser.parse(
            "https://medium.com/feed/tag/hiring"
        )
    for i in range(10):
        info = url.entries[i]
        content= HiringContent()
        content.headline= info.title
        #-----finding image link
        desc = info.description
        start=desc.find("img src=")
        end=desc.find("width")
        
        print(desc[end:])
        desc=desc[start+9:end-2:]
        print("-----------------------------")
        print(desc)

        #---------------
        content.img = desc
        content.url  = info.link
        content.save()
    
    return redirect('/')

def home(request):
    
    pycontent = PyContent.objects.all()
    progcontent = ProgContent.objects.all()
    hiringcontent = HiringContent.objects.all()
    covidcontent = CovidContent.objects.all()
    context = { 
        'pycontent': pycontent,
        'progcontent': progcontent,
        'hiringcontent': hiringcontent,
        'covidcontent': covidcontent,
    }
    return render(request,'app/home.html',context)
