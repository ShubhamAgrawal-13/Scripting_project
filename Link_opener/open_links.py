import time
from sys import argv
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("../chromedriver")
#driver=webdriver.Firefox()

filename=""
if(len(argv)<=1):
	filename="lab_links.txt"
else:
	filename=str(argv[1])



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
