import requests 
from bs4 import BeautifulSoup 
from playsound import playsound
import time
import sys

print('Live Cricket Matches:')
url = "http://static.cricinfo.com/rss/livescores.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html5lib')

i = 1
for item in soup.findAll('item'):
	print(str(i) + '. ' + item.find('description').text)
	i = i + 1

links = []    
for link in soup.findAll('item'):
	links.append(link.find('guid').text)

print('Enter match number or enter 0 to exit:')
userInput = int(input())

URL = links[userInput - 1]
print(URL)
# URL = "https://www.espncricinfo.com/series/19309/game/1193497/afghanistan-vs-west-indies-1st-odi-west-indies-in-india-2019-20"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
oldover=0.0
while(True):
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html5lib')
	ll=soup.findAll('div',{'class':'time-stamp'})
	recentover=(float)(ll[0].get_text())
	print("Overs : ",recentover)
	lt=soup.findAll('div',{'class':'cscore_score'})
	score=lt[0].get_text()
	print("Score : ",lt[0].get_text())
	# ll1=soup.findAll('span',{'class':'over-score'})
	ll1=soup.findAll('div',{'data-reactid':'308'})
	tem=soup.findAll('div',{'class':'recent-overs-wrapper'})
	recentscore=tem[0].text[6]
	print("Current Ball : ",tem[0].text[6])
	#tt=tem[0].findAll('div',{'class':'label'})[0]
	# print(tt['data-reactid'])
	#print(ll1[0].get_text())
	#recentscore=ll1[0].get_text()
	#print(recentscore)
	# time.sleep(10)

	if((recentscore=="4") and (recentover-oldover>0)):
		playsound('four.mp3')	
	elif((recentscore=="6") and (recentover-oldover>0)):
		playsound('six.mp3')	
	elif((recentscore=="W") and (recentover-oldover>0)):
		playsound('wicket.mp3')	
	time.sleep(10)
	oldover=recentover

