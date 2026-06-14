from selenium import webdriver
from Pages.button_int_quota_page import ButtonIntQuota
from Pages.main_page import MainPage
import unittest

browser = webdriver.Chrome()
url = 'http://127.0.0.1:8080/'


class TestQuots(unittest.TestCase):
    def test1(self):
        x = MainPage(browser)
        y = ButtonIntQuota(browser)
        browser.get(url)
        x.int_quota_button_and_click()
        y.entering_into_a_line_name('A')
        y.entering_into_a_line_value(10)
        y.button_save_click()

    def test2(self):
        x = MainPage(browser)
        y = ButtonIntQuota(browser)
        browser.get(url)
        x.num_quota_and_click(0)
        y.clear_input_name()
        y.clear_input_value()
        y.entering_into_a_line_name('ASd')
        y.entering_into_a_line_value(120)
        y.button_save_click()

    def test3(self):
        x = MainPage(browser)
        browser.get(url)
        x.click_button_del(0)
        x.alert()
