from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


# class TestUserAddToBasketFromProductPage():

#     pass

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



# urls_common_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# # 7th url contain an error which will not supposed to be debugged
# urls_list = [f'{urls_common_base}{n}' for n in range(10) if n != 7]

# @pytest.mark.parametrize('urls_list', [*urls_list, 
#                                       pytest.param(f'{urls_common_base}7', marks=pytest.mark.xfail)]) 
# def test_guest_can_add_product_to_basket(browser, urls_list):
#     print(urls_list)
#     page = ProductPage(browser, urls_list)
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

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"
#     page = ProductPage(browser, link)
#     page.open()
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


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-clean-coder_150/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    # Ожидаем, что в корзине нет товаров
    page.should_be_basket_empty()
    # Ожидаем, что есть текст о том что корзина пуста 
    page.should_be_message_basket_is_empty()
