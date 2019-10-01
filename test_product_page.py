from .pages.product_page import Page_Object
import pytest

@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])

def test_guest_can_add_product_to_basket(browser, promo_code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}"
    print(link)
    page = Page_Object(browser, link)
    page.open()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    page.check_after_add_product_to_basket()








