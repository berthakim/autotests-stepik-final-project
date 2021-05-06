# file: product_page.pyt
# ...
    # def should_be_message_of_success(self):
    #     # check if the message present
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_SUCCES), "No message"  # you call this same method twice
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name isn't present on page"
        
    #     # check if it's a correct message (having the correct name of product)
    #     product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_SUCCES).text
    #     product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    #     assert product_name_in_message == product_name, "Product wasn't added (name of product is not in message)"

    # def should_be_price_of_cart(self):
    #     # check if the message present
    #     assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE), "No message of price"
    #     assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT), "Price of product isn't correct"

    #     # check if the price is correct
    #     price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
    #     price_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
    #     assert price_message == price_message, "Price in message doesn't equalt to price of product"

# ....
