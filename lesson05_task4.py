from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get("http://the-internet.herokuapp.com/login")

username_input = browser.find_element(By.CSS_SELECTOR, '#username')
username_input.send_keys('tomsmith')
sleep(5)

password_input = browser.find_element(By.CSS_SELECTOR, '#password')
password_input.send_keys('SuperSecretPassword!')
sleep(5)

button = browser.find_element(By.CSS_SELECTOR, 'button')
button.click()
sleep(5)

text = browser.find_element(By.CSS_SELECTOR, '#flash').text

print(text)
