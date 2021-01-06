import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

time.sleep(10)
searchbox = driver.find_element_by_xpath("//div[@id='side']/div[1]/div/label/div/div[2]")
//Enter the name of the person you want to send the message to
searchbox.send_keys('person name')
searchbox.send_keys(Keys.ENTER)
time.sleep(10)
inputbox = driver.find_element_by_xpath("//div[@id='main']/footer/div[1]/div[2]/div/div[2]")
//Enter the the message that you want to be sent
inputbox.send_keys('message')
inputbox.send_keys(Keys.ENTER)
