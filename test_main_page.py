from .pages.product_page import Page_Object
import pytest
import time

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = Page_Object(browser, link)
    page.open()
    page.go_to_basket_from_main()
    page.check_empty_basket()
    page.check_message_in_empty_basket()