# autoweb.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = r'C:\Users\Hery\Desktop\Python Bootcamp 2022\Auto Web Selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.pantip.com/forum/wahkor'
driver.get(url)

driver.maximize_window()
# driver.save_screenshot(r'test.png')

# forward
for i in range(5):
	driver.execute_script('window.scrollTo(0, {})'.format(10000*i))
	time.sleep(2)

# backward
for i in reversed(range(5)):
	driver.execute_script('window.scrollTo(0, {})'.format(10000*i))
	time.sleep(2)

# capture
for i in range(60):
	driver.execute_script('window.scrollTo(0, {})'.format(800*i))
	driver.save_screenshot('pantip-{}.png'.format(i))
