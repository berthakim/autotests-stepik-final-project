from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_FORM_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-noicon.alert-info > .alertinner")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main :nth-child(2)")  # .product_main > .price_color


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")  # .btn-group :nth-child(1)
    BASKET_FORM = (By.ID, "#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
