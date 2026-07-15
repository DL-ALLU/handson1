from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.get("https://practicetestautomation.com/practice-test-login/")
print("Open Browser")
time.sleep(2)
browser.maximize_window()
title = browser.title
print(title)
time.sleep(2)
browser.quit()
