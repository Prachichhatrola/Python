from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup = chrome_browser.find_element(By.ID, "at-cv-lightbox-close")
popup.click()


user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I AM EXTRA COOOOL")

time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-default")
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, "display")
assert "I AM EXTRA COOOOL" in output_message.text
