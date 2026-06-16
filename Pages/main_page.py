from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import BasePage


class MainPage(BasePage):
    selector_button = (By.ID, "create-integer")
    selector_class_quot = (By.CLASS_NAME, 'mb-4.object-item')
    selector_button_del = (By.CSS_SELECTOR, '[data-qa="list-item-delete"]')
    selector_list_quot = (By.CLASS_NAME, 'mb-4.object-item')
    check = []

    def int_quota_button_and_click(self, ):
        """Находит и кликает на кнопку создания квоты"""
        self.find(self.selector_button).click()

    def num_quota_and_click(self, num: int):
        """Кликает на элемент списка квот"""
        self.finds(self.selector_list_quot)[num].click()

    def click_button_del(self, num: int):
        """Находит и кликает на кнопку удаления квоты"""
        actioncains = ActionChains(self.browser)
        list_quots = self.finds(self.selector_class_quot)[num]
        actioncains.move_to_element(list_quots).move_to_element(self.find(self.selector_button_del)).click().perform()

    def alert(self):
        "Закрывает алерт"
        self.alert = self.browser.switch_to.alert
        self.alert.accept()

    #def checks_the_name(self, num: int, check: str):
        #"""Проверяет совпадает-ли имя """
        #name = self.finds(self.selector_list_quot)[num]
        #name_text = name.find_element(By.CLASS_NAME, "item-name").text
        #assert name_text == check

    #def checks_the_value(self, num: int, check: int):
        #"""Проверяет совпадает-ли значение """
        #value = self.finds(self.selector_list_quot)[num]
        #value_text = int(value.find_element(By.CLASS_NAME, "item-value").text)
        #assert value_text == check

    def saves_the_name_and_value(self, num: int):
        """Сохраняет имя и значение кворты"""
        quot = self.finds(self.selector_list_quot)[num]
        name = quot.find_element(By.CLASS_NAME, "item-name").text
        value = quot.find_element(By.CLASS_NAME, "item-value").text
        return self.check.extend([name, int(value)])

    def checking_name_and_value(self, num: int, check_name: str, check_value: int):
        """Проверка на идентичность"""
        self.saves_the_name_and_value(num)
        neme,value = self.check
        assert neme == check_name and value == check_value
        self.check = []

    def checking_for_changes(self):
        """Проверка изменения квоты"""
        assert self.check[0] != self.check[1]
        self.check =[]

    def cecking_del_quot(self,num:int):
        assert self.finds(self.selector_list_quot) == []
