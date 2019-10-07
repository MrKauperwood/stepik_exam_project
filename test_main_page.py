from .pages.product_page import ProductPage
from .pages.basket_page import Basket_Page
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = Basket_Page(browser, link)
    page.open()
    page.go_to_basket_from_main()
    page.check_empty_basket()
    page.check_message_in_empty_basket()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.skip
    def test_guest_should_see_login_link_(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()






