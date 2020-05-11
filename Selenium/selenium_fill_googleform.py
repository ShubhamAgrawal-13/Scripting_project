import time
from selenium import webdriver

driver=webdriver.Chrome("/home/shubham/Downloads/chromedriver_linux64/chromedriver")

# driver.get("http://www.google.com")
# box=driver.find_element_by_name('q')

# box.send_keys('iiit hyderabad')
# box.submit()

for i in range(0,5):
	driver.get("https://docs.google.com/forms/d/1gpI0VDm5GzCLySCGDJR0oIpPhj_O0ESky7snI6ZDerY/viewform?fbclid=IwAR0IjtcTZVYMPaHVBeKzQymqvyusYBBZ3FreZXzQLUbtqwkWKJs7RPNTXI8&edit_requested=true")
	box1=driver.find_element_by_name('entry.957312585')
	box1.send_keys('Bot'+str(i))
	time.sleep(2)
	box1=driver.find_element_by_name('entry.341595524')
	box1.send_keys('Awesome !')
	time.sleep(2)
	button=driver.find_element_by_xpath("//div[@class='freebirdFormviewerViewNavigationButtons']/div")
	button.click()
	time.sleep(4)
