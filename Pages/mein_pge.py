from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    #browser = webdriver.Chrome()
    #url = 'http://127.0.0.1:8080/'


    def __init__(self,browser,url):
        self.browser = browser
        self.url = url

    def open_page(self,url):
        "Открывает браузер"
        return self.browser.get(url)

    def int_quota_button_and_click(self):
        "Находит и кликает на кнопку создания квоты"
        int_button = self.browser.find_element(By.ID,"create-integer")
        return int_button.click()

    def list_quots(self):
        "Получает список квот"
        list_quots = self.browser.find_elements(By.CLASS_NAME, 'mb-4.object-item')
        return list_quots

    def element_from_list_quots(self,int):
        "Возвращает элемент из списка квот"
        return self.list_quots()[int]

    def element_from_list_quots_click(self):
        return self.element_from_list_quots().click()