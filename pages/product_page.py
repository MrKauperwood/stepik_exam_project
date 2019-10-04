from .base_page import BasePage
from .locators import ProductPageLocators


class Page_Object(BasePage):
    def check_after_add_product_to_basket(self):
        self.check_message_after_add_product()
        self.check_price_basket_total()
        self.check_price_basket_total2()

    def click_on_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        basket_button.click()

    def check_price_basket_total(self):
        assert self.get_text_message(*ProductPageLocators.PRICE_BOOK_ORIGINAL) in\
               self.get_text_message(*ProductPageLocators.PRICE_BOOK_AFTER_ADD1), "Prices are not equal (one)"

    def check_price_basket_total2(self):
        assert self.get_text_message(*ProductPageLocators.PRICE_BOOK_ORIGINAL) in\
               self.get_text_message(*ProductPageLocators.PRICE_BOOK_AFTER_ADD2), "Prices are not equal (two)"

    def check_message_after_add_product(self):
        assert self.get_text_message(*ProductPageLocators.NAME_OF_THE_BOOK_ORIGINAL) ==\
               self.get_text_message(*ProductPageLocators.INFO_ADD_TO_BASKET), "Product name other"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_item(self):
        assert self.is_disappeared(*ProductPageLocators.DISAPPEAR_ITEM), \
            "Element didn't disappeare, but should have been"