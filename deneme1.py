from email import header
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

import time 

# soup = BeautifulSoup( , 'html.parser')

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}

s = Service("/Users/yakupakyniyazov/Downloads/geckodriver")
browser = webdriver.Firefox(service=s)

browser.maximize_window()
browser.get("https://www.trendyol.com/butik/liste/2/erkek")
time.sleep(2)

browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/p").click()
time.sleep(2)

browser.find_element(By.XPATH,"//*[@id='login-email']").send_keys('yakup.akinyaz@gmail.com')
time.sleep(1)

browser.find_element(By.XPATH,"//*[@id='login-password-input']").send_keys('28Mart19y@')
time.sleep(2)

browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button").click()
time.sleep(1)

browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/p").click()
time.sleep(1)

browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div/div/a[1]/span").click()
time.sleep(1)

current_link = browser.current_url
r = requests.get(current_link)
print(r.content)

