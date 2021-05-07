from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    # Ожидаем, что в корзине нет товаров
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_FORM), \
        "Basket isn't empty, but should be"

    # Ожидаем, что есть текст о том что корзина пуста
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), \
        "No message about empty basket"
    
    # alternative version
    # def should_be_message_basket_is_empty(self):
    #     message = self.browser.find_element(*BasePageLocators.BASKET_EMPTY_MESSAGE).text
    #     assert "Your basket is empty" in message, "No message about empty basket"
