from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    page.solve_quiz_and_get_code()

    page.should_message_product_in_basket_equal_to_the_product_name()
    print("yes")
    page.should_message_price_of_product_in_basket_equal_to_product_price()
    print("yes")




