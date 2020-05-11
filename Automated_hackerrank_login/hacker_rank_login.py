import time
import getpass
import requests 
from bs4 import BeautifulSoup  
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys


#driver=webdriver.Firefox()

lgn=0

def login():
	global lgn
	global driver
	if(lgn==0):
		username=input("Enter username : ")
		password=getpass.getpass(prompt='Enter Password: ', stream=None)
		print(username) #,password)
		driver=webdriver.Chrome("../chromedriver")
		driver.get("https://www.hackerrank.com/auth/login")
		box1=driver.find_element_by_name('username')
		box1.send_keys(username)
		time.sleep(2)
		box2=driver.find_element_by_name('password')
		box2.send_keys(password)
		time.sleep(2)
		button=driver.find_element_by_class_name("ui-btn.ui-btn-large.ui-btn-primary.auth-button")
		button.click()
		time.sleep(1)
		lgn=1
		print("login successfully")
	else:
		print("Already logged in")

def logout():
	global lgn
	global driver
	if(lgn==1):
		driver.get("https://www.hackerrank.com/dashboard")
		button=driver.find_element_by_class_name('backbone.nav_link.js-dropdown-toggle.js-link.toggle-wrap')
		button.click()
		time.sleep(1)
		button=driver.find_element_by_link_text('Logout')
		button.click()
		time.sleep(1)
		lgn=0
	else:
		print("first login")

# def userinfo(name):
# 	URL="https://www.hackerrank.com/"+name
# 	r = requests.get(URL)
# 	soup = BeautifulSoup(r.content, 'html5lib')
# 	ll=soup.find(class_='hacker-badges-section')
# 	# print(soup)
# 	print(ll)

	# print("Name of user : ",ll.get_text())




def open_aps_links():
	global driver
	global lgn
	if(lgn==1):
		pass
	else:
		driver=webdriver.Chrome("../chromedriver")
	f=open("lab_links.txt","r")
	list_of_links=f.readlines()
	# print(list_of_links)

	for i in range(0,len(list_of_links)-1):
		#driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

		# print("hello")
		try:
			driver.get(list_of_links[i])
			driver.execute_script("window.open('');")
			Window_List = driver.window_handles	
			driver.switch_to_window(Window_List[-1])
		except:
			print("check internet connection")
			pass
	try:	
		driver.get(list_of_links[len(list_of_links)-1])
	except:
		print("check internet connection")

def open_links(filename):
	global driver
	f=open(filename,"r")
	list_of_links=f.readlines()
	# print(list_of_links)

	for i in range(0,len(list_of_links)-1):
		#driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

		# print("hello")
		try:
			driver.get(list_of_links[i])
			driver.execute_script("window.open('');")
			Window_List = driver.window_handles	
			driver.switch_to_window(Window_List[-1])
		except:
			print("check internet connection")
			pass
	try:	
		driver.get(list_of_links[len(list_of_links)-1])
	except:
		print("check internet connection")


driver=0
while(1):
	print("------------Automated hackerrank------------")
	print("1: for hackerrank login")
	print("2: for opening all APS lab links at once")
	print("3: for opening all other links at once")
	# print("4: for user details")
	print("4: for logout")
	print("5: for Exit")

	choice=input("Enter your choice : ")
	if(choice=="1"):
		login()
		print("completed 1")
	elif(choice=="2"):
		open_aps_links()
		print("completed 2")
	elif(choice=="3"):
		filename=input("Enter file name : ")
		open_links(filename)
		print("completed 3")
	# elif(choice=="4"):
	# 	name=input("Enter name to find user info : ")
	# 	userinfo(name)
	# 	print("completed 4")
	elif(choice=="4"):
		logout()
		print("completed 4")
	elif(choice=="5"):
		print("Exiting... ")
		break
	else:
		print("Please Enter value in between 1 - 5")

print("Bye")


# profile-heading
