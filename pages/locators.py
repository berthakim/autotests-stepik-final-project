from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_SUCCES = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-noicon.alert-info > .alertinner")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main :nth-child(2)")  # .product_main > .price_color
