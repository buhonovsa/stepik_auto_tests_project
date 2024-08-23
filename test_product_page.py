from stepik_auto_tests_project.pages.product_page import ProductPage
#from selenium.common.exceptions import NoAlertPresentException
import time

def test_guest_add_product_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_cart()
    time.sleep(20)
     

