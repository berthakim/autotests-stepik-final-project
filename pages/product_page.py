from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def add_article_to_cart(self):  # with promo-code
        self.should_be_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)  # you call this same method twice
        button.click()
        self.solve_quiz_and_get_code()  # BasePage's method
        self.should_be_message_of_success()
        self.should_be_product_name_message_equal_to_name()
        self.should_be_price_of_cart()
    
    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "Button doesn't exist"

    def should_be_message_of_success(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE), "No message"  # you call this same method twice
        
    def should_be_product_name_message_equal_to_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
        "Product name isn't present on page"

        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_message == product_name, \
        "Name of product in message != name product added to basket"

    def should_be_price_of_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE), "No message of price"

    def should_be_cart_price_equal_to_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT), \
        "Price of product isn't correct"

        price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price_message == price_message, \
        "Price in message doesn't equal to price of product"

    def should_not_be_success_message(self):
    	assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_desappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not desappeared, but should"
