from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    
    def add_article_to_cart(self):  # with promo-code
        self.should_be_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)  # you call this same method twice
        button.click()
        try:
            self.solve_quiz_and_get_code()
        except (NoAlertPresentException):
            pass

    def should_be_messages_after_adding_products(self):
        self.should_be_success_message()
        self.should_be_price_of_basket()
    
    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "Button doesn't exist"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), "No message"  # you call this same method twice
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
        "Product name isn't present on page"
        # check if product'sname in message match with name of added product
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_message == product_name, \
        "Name of product in message != name product added to basket"

    def should_be_price_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE), "No message of price"
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT), \
        "Price of product isn't correct"
        # check if he price in message equal to price of product
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price_message == price_message, \
        "Price in message doesn't equal to price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_desappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), \
        "Success message is not desappeared, but should"
