from selenium import webdriver
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
time.sleep(2)