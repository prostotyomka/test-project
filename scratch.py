from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
url = 'http://127.0.0.1:8080/'

browser.get(url)
browser.find_element(By.ID,"create-integer").click()
browser.find_element(By.NAME,'quota_name').send_keys('Artom')
browser.find_element(By.NAME,'object_value').send_keys(10)
browser.find_element(By.ID,'i-save').click()

x = browser.find_elements(By.CLASS_NAME,'mb-4.object-item')
x[0].click()
browser.find_element(By.NAME,'object_value').clear()
browser.find_element(By.NAME,'object_value').send_keys(12)
browser.find_element(By.ID,'i-save').click()

len_1 = browser.find_elements(By.CLASS_NAME,'mb-4.object-item')
button = browser.find_element(By.XPATH,'/html/body/div/div[2]/table/tbody/tr/td[4]/button[2]')
actioncains = ActionChains(browser)
actioncains.move_to_element(len_1[0]).move_to_element(button).click().perform()
alert = browser.switch_to.alert
alert.accept()

