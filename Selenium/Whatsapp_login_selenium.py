import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("/home/shubham/Downloads/chromedriver_linux64/chromedriver")

# driver.get("http://www.google.com")
# box=driver.find_element_by_name('q')

# box.send_keys('iiit hyderabad')
# box.submit()

for i in range(0,1):
	driver.get("https://web.whatsapp.com/")
	a=input("Press enter to continue ! ")
	name=driver.find_element_by_css_selector('._2zCfw.copyable-text.selectable-text')
	name.send_keys("Shrayans Jain")
	name.send_keys(Keys.ENTER)
	time.sleep(2)

	for i in range(0,10):
		msg=driver.find_element_by_css_selector('._3u328.copyable-text.selectable-text')
		msg.send_keys("I am a bot :) "+str(i))
		msg.send_keys(Keys.ENTER)
		time.sleep(2)