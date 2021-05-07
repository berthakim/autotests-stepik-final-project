from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
from string import ascii_lowercase
from random import randint, choice
import time


@pytest.mark.register_guest
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        letters = ascii_lowercase
        email = "".join(choice(letters) for i in range(8)) + "@mail.org"
        password = randint(10**8, 10**9)

        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        # time.sleep(10)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"
        page = ProductPage(browser, link)
        page.open()
        page.add_article_to_cart()
        page.should_be_messages_after_adding_products()


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/fr/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_article_to_cart()
#     page.should_be_messages_after_adding_products()

# def test_guest_can_add_product2_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_article_to_cart()
#     page.should_be_messages_after_adding_products()


# @pytest.mark.xfail(reason="negative check")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_article_to_cart()
#     page.should_not_be_success_message()

# @pytest.mark.xfail(reason="negative check")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_article_to_cart()
#     page.should_desappear_success_message()



# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     # инициализируем Page Object, 
#     # передаем в конструктор экземпляр драйвера и url адрес
#     page = ProductPage(browser, link)
#     page.open()
#     # выполняем метод страницы — переходим на страницу логина
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-clean-coder_150/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.go_to_basket()
#     # Ожидаем, что в корзине нет товаров
#     page.should_be_basket_empty()
#     # Ожидаем, что есть текст о том что корзина пуста 
#     page.should_be_message_basket_is_empty()
