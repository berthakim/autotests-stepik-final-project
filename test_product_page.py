from .pages.product_page import ProductPage
import pytest


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/fr/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_article_to_cart()

# def test_guest_can_add_product2_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_article_to_cart()

urls_common_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# 7th url contain an error which will not supposed to be debugged
urls_list = [f'{urls_common_base}{n}' for n in range(10) if n != 7]

@pytest.mark.parametrize('urls_list', [*urls_list, 
	                                  pytest.param(f'{urls_common_base}7', marks=pytest.mark.xfail)]) 
def test_guest_can_add_product_to_basket(browser, urls_list):
    print(urls_list)
    page = ProductPage(browser, urls_list)
    page.open()
    page.add_article_to_cart()
