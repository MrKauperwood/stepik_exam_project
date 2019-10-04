from .pages.product_page import Page_Object
import pytest
import time

#@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
#@pytest.mark.parametrize('promo_code', [0])

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Page_Object(browser, link)
    page.open()
    page.click_on_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Page_Object(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Page_Object(browser, link)
    page.open()
    page.click_on_basket_button()
    page.should_disappear_item()

"""
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}"
    page = Page_Object(browser, link)
    page.open()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    page.check_after_add_product_to_basket()
"""








