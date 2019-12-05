from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "#login_form")
    REGISTER_FORM = (By.CLASS_NAME, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-lg.btn-primary")
    ALERT_LOCATOR = (By.CLASS_NAME, "alert-safe")
    PRODUCT_LOCATOR = (By.CLASS_NAME, "product_main")
    PRODUCT_NAME = (By.CLASS_NAME, "product_main")
