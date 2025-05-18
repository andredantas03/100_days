import time

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')

soup = BeautifulSoup(response.text, 'html.parser')

list = soup.select('span.PropertyCardWrapper__StyledPriceLine')

links = [i.get('href') for i in soup.select('a.property-card-link')]
addresses = [i.getText().strip().replace('|','') for i in soup.select('div a address')]
prices = []

for i in list:
    text = i.getText()
    pattern = r'\$\d{1},?\d{3}'
    price = re.match(pattern,text)
    prices.append(price.group())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):
    driver.get(url='https://forms.gle/p2V7pb7hNzNirPLz6')
    time.sleep(2)

    question1 = driver.find_element(by=By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    question1.send_keys(addresses[n])
    question2 = driver.find_element(by=By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    question2.send_keys(prices[n])
    question3 = driver.find_element(by=By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    question3.send_keys(links[n])

    submit = driver.find_element(by=By.CSS_SELECTOR, value='#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span')

    time.sleep(3)
    submit.click()