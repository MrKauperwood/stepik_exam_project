from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators, MainPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def check_empty_basket(self):
        assert self.is_not_element_present(*MainPageLocators.ALL_ITEMS_IN_BASKET), \
            "The basket is not empty, but should be"

    def check_message_in_empty_basket(self):
        assert "Your basket is empty." in \
            self.get_text_message(*MainPageLocators.INFO_BUSKET_IS_EMPTY), "No -Empty basket- message"