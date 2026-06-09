from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'http://127.0.0.1:8080/'

browser.get(url)
browser.find_element(By.ID,"create-integer").click()
browser.find_element(By.NAME,'quota_name').send_keys('Artom')
browser.find_element(By.NAME,'object_value').send_keys(10)
browser.find_element(By.ID,'i-save').click()
time.sleep(2)


x = browser.find_elements(By.CLASS_NAME,'mb-4.object-item')
x[0].click()
browser.find_element(By.NAME,'object_value').clear()
browser.find_element(By.NAME,'object_value').send_keys(12)
browser.find_element(By.ID,'i-save').click()
time.sleep(2)

