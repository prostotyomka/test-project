from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'http://127.0.0.1:8080/'

browser.get(url)