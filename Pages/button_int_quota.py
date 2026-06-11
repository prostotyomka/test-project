from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.mein_pge import BasePage

c = 'Artem'
#browser = webdriver.Chrome()
#url = 'http://127.0.0.1:8080/'

class Button_int_quota(BasePage):

    def __init__(self, browser, url, str):
        super().__init__(browser, url)
        self.str = str

    def name_input(self):
        "Поле ввода имени"
        return self.browser.find_element(By.NAME, 'quota_name')

    def entering_into_a_line_name(self,str):
        "Водит имя в поле имени"
        name_input = self.name_input()
        return name_input.send_keys(str)

    def value_input(self):
        "Поле ввода значения"
        return self.browser.find_element(By.NAME,'object_value')

    def entering_into_a_line_value(self,str):
        "Вводит значение в поле значения"
        input_value = self.value_input()
        return input_value.send_keys(str)

    def button_save(self):
        "Кнопка сохранить"
        return self.browser.find_element(By.ID,'i-save')

    def button_save_clicl(self):
        "Кликает на кнопку сохранить"
        button_save = self.button_save()
        return button_save.click()


