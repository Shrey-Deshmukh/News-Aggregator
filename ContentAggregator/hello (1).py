import feedparser
import requests
import re
from bs4 import BeautifulSoup

print("hello")

dis = requests.get(" https://www.thehindu.com/")
dis_soup = BeautifulSoup(dis.content, 'html5lib')
dis_headings = dis_soup.find_all('div',{'class':'story-card'})
news_title = []
news_images = []
news_url = []
#print(dis_headings)
for article in dis_headings:
    #print(article)
    #print("###############################################")
    main1 = article.find_all('a')[0]    
    main1 = str(main1)
    #print(main1)
    link = re.findall(r'href=\"(.*?)\"', main1)
    imagelink = article.find_all('img')[0]
    imagelink = str(imagelink)
    image = re.findall(r'data-src-template=\"(.*?)\"', main1)
    #print(link) 
    title = article.find_all('h2')
    
    title = str(title)

    title1 = title.split("\n")
    #news_title =  dis_soup.findAll("h2")[0].renderContents()
    #print(len(title1))
    link = str(link)
    #print(link[10:-2])
    image = str(image)
    #print(image[10:-2])
    #title = title.split()
    if len(title1) != 1:
        news_title.append(title1[2])
        news_images.append(image[2:-2])
        news_url.append(link[2:-2])
    #print(main)
    #print(link)


for i in range(len(news_title)):
         
   
       print(str(news_title[i]))

       print(str(news_url[i]))

       print(str(news_images[i]))
        

