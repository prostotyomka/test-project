from selenium import webdriver

from Pages.button_int_quota import Button_int_quota
from Pages.mein_pge import BasePage

browser = webdriver.Chrome()
url = 'http://127.0.0.1:8080/'

main_page = BasePage(browser,url)
int_quot = Button_int_quota(browser,url,str)

main_page.open_page(url)
main_page.int_quota_button_and_click()
int_quot.entering_into_a_line_name(str='Art')
int_quot.entering_into_a_line_value(str="10")
int_quot.button_save_clicl()




print('Я сделал')


