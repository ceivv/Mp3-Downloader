from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

songName= input('give song name :')
url='https://www.youtube.com/results?search_query='+songName
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
mylist=[]
for link in soup.find_all('a',href=True):
	if '/watch?v=' in link['href']:
		mylist.append(link['href'])
songLink='https://www.youtube.com/'+mylist[0]

br=webdriver.Firefox()
br.get('https://ytmp3.cc/en/')
link=br.find_element_by_xpath('//*[@id="input"]')
link.send_keys(songLink)
link.submit()
time.sleep(3)#wait two seconds before clicking download to let the website reloads
link2=br.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
try:
	link2.click()
except:
	print('oops cannot open link!!!')


input('hhh')