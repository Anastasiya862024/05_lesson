from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get('http://uitestingplayground.com/classattr')

button = browser.find_element(By.CLASS_NAME, 'btn-primary')
button.click()
sleep(5)

browser.quit()
