from selenium import webdriver
from Pages.button_int_quota_page import ButtonIntQuota
from Pages.main_page import MainPage
import unittest

browser = webdriver.Chrome()
url = 'http://127.0.0.1:8080/'
class TestQuots(unittest.TestCase):
    def setUp(self):
        self.main_page = MainPage(browser)
        self.button_qota = ButtonIntQuota(browser)
        browser.get(url)
    def test1(self):

        self.main_page.int_quota_button_and_click()
        self.button_qota.entering_into_a_line_name('A')
        self.button_qota.entering_into_a_line_value(10)
        self.button_qota.button_save_click()
        """Проверки"""
        self.main_page.checks_the_name(0,"A")
        self.main_page.checks_the_value(0,10)


    def test2(self):

        self.main_page.num_quota_and_click(0)
        self.button_qota.clear_input_name()
        self.button_qota.clear_input_value()
        self.button_qota.entering_into_a_line_name('B')
        self.button_qota.entering_into_a_line_value(120)
        self.button_qota.button_save_click()
        """Проверки"""
        self.main_page.checks_the_name(0,"B")
        self.main_page.checks_the_value(0,120)

    def test3(self):

        self.main_page.click_button_del(0)
        self.main_page.alert()
        """Проверкаа"""
        self.main_page.cecking_del_quot(0)
