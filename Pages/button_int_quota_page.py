from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class ButtonIntQuota(BasePage):
    selector_name_input = (By.NAME, 'quota_name')
    selector_value_input = (By.NAME, 'object_value')
    selector_button_save = (By.ID, 'i-save')


    def entering_into_a_line_name(self, name: str):
        """Водит имя в поле имени"""
        self.find(self.selector_name_input).send_keys(name)

    def entering_into_a_line_value(self, value):
        """Вводит значение в поле значения"""
        self.find(self.selector_value_input).send_keys(value)

    def button_save_click(self):
        """Кликает на кнопку сохранить"""
        self.find(self.selector_button_save).click()

    def clear_input_name(self):
        """Очищает строку ввода имени"""
        self.find(self.selector_name_input).clear()

    def clear_input_value(self):
        """Очищает строку ввода значения"""
        self.find(self.selector_value_input).clear()


