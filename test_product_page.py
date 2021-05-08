from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
from string import ascii_lowercase
from random import randint, choice


# link to one frequently used link
link_book = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"


# The class below is not a good practice. Only for demonstration
@pytest.mark.register_guest
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        letters = ascii_lowercase
        email = "".join(choice(letters) for _i in range(8)) + "@mail.org"
        password = randint(10**8, 10**9)
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = link_book
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = link_book
        page = ProductPage(browser, link)
        page.open()
        page.add_article_to_cart()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = link_book
    page = ProductPage(browser, link)
    page.open()
    page.add_article_to_cart()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-clean-coder_150/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_empty()
    page.should_be_message_basket_is_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # initialize a Page Object
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# negative check 1
@pytest.mark.xfail(reason="negative check")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = link_book
    page = ProductPage(browser, link)
    page.open()
    page.add_article_to_cart()
    page.should_not_be_success_message()


# negative check 2
@pytest.mark.xfail(reason="negative check")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = link_book
    page = ProductPage(browser, link)
    page.open()
    page.add_article_to_cart()
    page.should_desappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# same test as above but with parametrization (test_guest_can_add_product_to_basket)
urls_common_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# 7th url contain an error which is not supposed to be debugged
urls = [f'{urls_common_base}{n}' for n in range(10) if n != 7]
urls_to_check = [*urls, pytest.param(f'{urls_common_base}7', marks=pytest.mark.xfail)]


@pytest.mark.skip()
@pytest.mark.parametrize('urls_list', urls_to_check)
def test_guest_can_add_product_to_basket_with_parametrize(browser, urls_list):
    link = link_book
    page = ProductPage(browser, link)
    page.open()
    page.add_article_to_cart()
