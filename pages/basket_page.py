from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    # basket should be empty
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_FORM), \
            "Basket isn't empty, but should be"

    # waiting for a message saying that basket is empty
    def should_be_message_basket_is_empty(self):
        message = self.browser.find_element(*BasePageLocators.BASKET_EMPTY_MESSAGE).text
        assert "Your basket is empty" in message, "No message about empty basket"
