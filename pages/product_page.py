from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def add_article_to_cart(self):
        self.should_be_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)  # you call this same method twice
        button.click()
        if "promo" in self.url:
            self.solve_quiz_and_get_code()
        # check messages after adding product:
        self.should_be_success_message()
        self.should_be_success_message_containing_product_name()
        self.should_be_price_message()
        self.should_be_price_of_basket_in_message()

    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "Button doesn't exist"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), \
            "No message at all"

    def should_be_success_message_containing_product_name(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_message == product_name, \
            "Name of product in message != name product added to basket"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE), "No message of price"

    # check if he price in message equal to price of product
    def should_be_price_of_basket_in_message(self):       
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price_product == price_message, "Price in message doesn't equal to price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_desappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), \
            "Success message is not desappeared, but should"
