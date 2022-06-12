# autoweb.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

op = webdriver.ChromeOptions()
op.add_argument('headless')

path = Service(r'C:\Users\Hery\Desktop\Python Bootcamp 2022\Auto Web Selenium\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=path, options=op)

# search = driver.find_element_by_name('q')
# search.send_keys('Manchester United')
# search.send_keys(Keys.RETURN) # press enter

url = 'http://www.uncle-machine.com/login'
driver.get(url)

# --------------LOGIN--------------

username = driver.find_element(By.ID, 'username')
username.send_keys('hery2323@gmail.com')

password = driver.find_element(By.ID, 'password')
password.send_keys('123456')

button = driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
button.click()

time.sleep(2)

url2 = 'http://www.uncle-machine.com/sensor/'
driver.get(url2)

sensor_id = driver.find_element(By.ID, 'sid')
sensor_id.send_keys('SID-1001')
sensor_id.send_keys(Keys.RETURN)

time.sleep(1)

temp = driver.find_element(By.CLASS_NAME, 'temp')
humid = driver.find_element(By.CLASS_NAME, 'humid')

print(temp.text, humid.text)

driver.close()

