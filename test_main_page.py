from .pages.product_page import Page_Object
from .pages.basket_page import Basket_Page
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = Basket_Page(browser, link)
    page.open()
    page.go_to_basket_from_main()
    page.check_empty_basket()
    page.check_message_in_empty_basket()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()