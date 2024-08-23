from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    FORM_REG = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED = (By.CLASS_NAME, "alertinner")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    
