from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("http://the-internet.herokuapp.com/inputs")

number_input = browser.find_element(By.CSS_SELECTOR, 'input')
number_input.send_keys(1000, Keys.RETURN)
sleep(5)

number_input.clear()
sleep(5)

number_input = browser.find_element(By.CSS_SELECTOR, 'input')
number_input.send_keys(999, Keys.RETURN)
sleep(5)

browser.quit()
