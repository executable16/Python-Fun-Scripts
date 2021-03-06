# Get the latest News From NDTV

############ Created By - Aditya Kulkarni ##############

# Requirements for running the script ->
# 		-> BeautifulSoup
# 		-> Requests

# For running the script -
#		-> python latestNews.py

# We can get the Big news as well as Top 10 news from www.ndtv.com
import requests 
from bs4 import BeautifulSoup 
import random 
r = requests.get('https://www.ndtv.com/')
soup1 = BeautifulSoup(r.content,'html5lib')
a = soup1.findAll('div',class_='featured_desc')
print('\t\t\t##################### BIG STORY ######################\n')
for i in a:
    print('\t\t'+i.text)
print('\n\t\t\t##########################################################\n')    
print('\n\n\n\t **************************************** Top 10 Stories ************************************** \n\n')  
f_con = soup1.findAll('div',class_='featured_cont')
uls = f_con[0].findAll('ul')
lis = uls[0].findAll('li')
cnt = 0
links = []
#print(lis)
for j in range(len(lis)):
    lk = lis[j].find('a')
    links.append(lk['href'])
headlines = []
for l in lis:

    headlines.append(l.text.strip())
for i in range(10):
    print('\n\t\t\t ############### News number ' + str(i+1)+' ##################\n')
    print('\t\t\t\n'+headlines[i]+"\n")
    print('To Read more - '+links[i]+'\n')
    