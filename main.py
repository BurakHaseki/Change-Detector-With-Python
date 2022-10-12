from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

URL = "URL_HERE"
TELEGRAM_BOT_TOKEN = "TOKEN_HERE"
TELEGRAM_CHAT_ID = "CHAT_ID_HERE"

def login_and_get_source(url):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    username = browser.find_element("xpath",'USERNAME_INPUT_XPATH_HERE')
    password = browser.find_element("xpath",'PASSWORD_INPUT_XPATH_HERE')
    username.send_keys("USERNAME_HERE")
    password.send_keys("PASSWORD_HERE")
    time.sleep(2)
    login = browser.find_element("xpath",'LOGIN_BUTTON_XPATH_HERE')
    login.click()
    time.sleep(2)
    html_source_code = browser.execute_script("return document.body.innerHTML;")
    html_soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')
    browser.close()
    return html_soup
    
source = login_and_get_source(URL)
message = "There is a change on the page. Check now: " + URL

while True:
    snap = login_and_get_source()
    if(snap != source):
        requests.post(url="https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_BOT_TOKEN),data={"chat_id":TELEGRAM_CHAT_ID,"text":message}).json()
        source = snap
        time.sleep(60)
    else:
        time.sleep(60)
