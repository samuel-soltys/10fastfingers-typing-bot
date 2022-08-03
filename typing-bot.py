import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome('D:\Bot_Nvidia_RTX\chromedriver.exe')

browser.get("https://10fastfingers.com/login")

user_email = os.environ.get('USER')
user_password = os.environ.get('PASSWORD')

browser.find_element_by_id("UserEmail").send_keys(user_email)
browser.find_element_by_id("UserPassword").send_keys(user_password)
browser.find_element_by_id("login-form-submit").click()

browser.get("https://10fastfingers.com/competition/6044d8762438f")

inputfield = browser.find_element_by_id("inputfield")

words = []
text = ""
time.sleep(5)
last_word = 0

for j in range(330):
    for i in range(last_word, 330):
        text = browser.find_element_by_xpath(f"//span[@wordnr='{i}']").text
        
        if text != '':
            words.append(text)
        else:
            last_word = i
            break
    if len(words) < 2:
        break
    for word in words:
        inputfield.send_keys(word + " ")
        time.sleep(0.08)
    words = []
    if last_word > 300:
        break

time.sleep(120)