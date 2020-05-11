import requests 
from bs4 import BeautifulSoup 
import csv

count=520
def phonelinks(link):
	URL = link
	ctn=0
	r = requests.get(URL) 
	soup = BeautifulSoup(r.content, 'html5lib') 
	fp = open("links_file.txt","a+")
	div=soup.find('div',attrs={'class':'makers'})
	# print(div)
	for link in div.findAll('a'):
		# print(link['href'])
		# print(link['href'])
		s="https://www.gsmarena.com/"
		s+=link['href']
		fp.write(s)
		fp.write("\n")
		ctn=ctn+1
	fp.close()
	return ctn


def write_data(link):
	r = requests.get(link) 
	soup = BeautifulSoup(r.content, 'html5lib') 
	modelname = soup.find('h1',attrs={"data-spec":"modelname"}).get_text()
	print(modelname)
	tables=soup.find_all('table')
	# print(tables)

	map={}

	for table in tables:
		header=table.find_all('th')[0].get_text()
		# data=table.find_all('td')
		datakey=table.find_all('td',attrs={'class':'ttl'})
		datavalue=table.find_all('td',attrs={'class':'nfo'})
		# print(header)
		for i in range(0,len(datakey)):
			# print(datakey[i].get_text(),end=":")
			# print(datavalue[i].get_text())
			# print(type(datakey[i].get_text()))

			if(datakey[i].get_text()=="SIM"):
				map["SIM"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="Size"):
				map["Size"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="OS"):
				map["OS"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="Chipset"):
				map["Chipset"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="CPU"):
				map["CPU"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="Internal"):
				map["Memory"]=datavalue[i].get_text()
			elif(header=="Main Camera"):
				map["Rear Camera"]=datavalue[i].get_text()
				break
			elif(header=="Selfie camera"):
				map["Front Camera"]=datavalue[i].get_text()
				# print("hii")
				break
			elif(datakey[i].get_text()=="WLAN"):
				map["Wifi"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="Bluetooth"):
				map["Bluetooth"]=datavalue[i].get_text()
			elif(datakey[i].get_text()=="Sensors"):
				map["Sensors"]=datavalue[i].get_text()
			elif(header=="Battery"):
				map["Battery"]=datavalue[i].get_text()
				break
			elif(datakey[i].get_text()=="Card slot"):
				map["Card slot"]=datavalue[i].get_text()
		# print('\n')
		#print('\n',table,'\n')

	spec_list=[]
	spec_list.append(modelname)
	for k,v in map.items():
		spec_list.append(v)
		# print(k,":",v,"\n")
	phone_list.append(spec_list)





URL = "https://www.gsmarena.com/makers.php3"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 

list_of_table_data=soup.findAll('td')

# for table_data in list_of_table_data:
# 	tt=table_data.findAll("a")
# 	print(tt)

div=soup.find('div',attrs={'class':'st-text'})

f = open("Brand_links.txt","w")
i=1
ctt=0
for link in div.findAll('a'):
	print(link['href'])
	# print(link.get_text())
	s="https://www.gsmarena.com/"
	s+=link['href']
	f.write(s)
	f.write("\n")
	k=phonelinks(s)
	print(k)
	ctt+=k
	if(ctt>count):
		break
	i+=1

f.close()




phone_list=[]

s="links_file.txt"
fp = open(s,"r")

links = fp.readlines()

print(ctt)
inc=1
try:	
	for link in links:
		write_data(link)
		print(inc,"*"*30)
		inc+=1
except:
	pass

# print(phone_list)
# dataset = pd.DataFrame(phone_list)
# dataset

features_list=["Name of Mobile Phone","SIM","Size","OS","Chipset","CPU","Card slot","Memory","Rear Camera","Front Camera","Wifi","Bluetooth","Sensors","Battery"]
with open("smartphone_dataset.csv","w",newline='') as f:
	w=csv.writer(f)
	w.writerow(features_list)
	for phone in phone_list:
		w.writerow(phone)

print("completed")

	


