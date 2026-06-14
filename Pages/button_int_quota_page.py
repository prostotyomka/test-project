from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class ButtonIntQuota(BasePage):
    selector_name_input = (By.NAME, 'quota_name')
    selector_value_input = (By.NAME, 'object_value')
    selector_button_save = (By.ID, 'i-save')

    def __init__(self, browser, ):
        super().__init__(browser)

    def name_input(self, ):
        """Поле ввода имени"""
        return self.find(self.selector_name_input)

    def entering_into_a_line_name(self, name: str):
        """Водит имя в поле имени"""
        self.name_input().send_keys(name)

    def value_input(self):
        """Поле ввода значения"""
        return self.find(self.selector_value_input)

    def entering_into_a_line_value(self, value):
        """Вводит значение в поле значения"""
        self.value_input().send_keys(value)

    def button_save(self):
        """Кнопка сохранить"""
        return self.find(self.selector_button_save)

    def button_save_click(self):
        """Кликает на кнопку сохранить"""
        self.button_save().click()

    def clear_input_name(self):
        self.name_input().clear()

    def clear_input_value(self):
        self.value_input().clear()


