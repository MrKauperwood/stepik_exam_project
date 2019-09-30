from selenium.webdriver.common.by import By


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_THE_BOOK_ORIGINAL = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    INFO_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) div")
    PRICE_BOOK_ORIGINAL = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_BOOK_AFTER_ADD1 = (By.CSS_SELECTOR, ".basket-mini")
    PRICE_BOOK_AFTER_ADD2 = (By.CSS_SELECTOR, ".alert-info .alertinner p:nth-child(1)")



