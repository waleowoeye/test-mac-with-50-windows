from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import bs4

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

news_pages=[]

driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")

'''
for element in soup.findAll('div', attrs={"class": "SbNwzf eeoZZ"}):
    print(element.a['href'])
'''

print ('*'*100)
for element2 in soup.findAll('h4', attrs={"class": "ipQwMb ekueJc RD0gLb"}):
    #print(element2.a['href'])
    news_pages.append(element2.a['href'])

print(len(news_pages))
for i in range(len(news_pages)):
    #print(news_pages[i])
    news_pages[i] = news_pages[i].replace(news_pages[i][:1], "https://news.google.com")
    #print(news_pages[i])

for j in news_pages:
    print(j)
    driver.get(j)
    driver.switch_to.new_window('window')




