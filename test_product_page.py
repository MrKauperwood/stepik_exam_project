from .pages.product_page import Page_Object


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Page_Object(browser, link)
    page.open()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    page.check_after_add_product_to_basket()







