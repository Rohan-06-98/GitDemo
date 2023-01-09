from selenium.webdriver.common.by import By


class Product_page:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart = (By.XPATH, "//input[@id='add-to-cart-button']")
    clik_to_cut_popup = (By.XPATH, "//a[@id='attach-close_sideSheet-link']")
    go_to_cart = (By.XPATH, "//a[@id='nav-cart']")
    click_on_proceed_to_pay = (By.XPATH, "//input[@name='proceedToRetailCheckout']")

    def addToCart(self):
        self.driver.find_element(*Product_page.add_to_cart).click()

    def cutPopup(self):
        self.driver.find_element(*Product_page.clik_to_cut_popup).click()

    def goToCart(self):
        self.driver.find_element(*Product_page.go_to_cart).click()

    def clickOnProceedToBuy(self):
        self.driver.find_element(*Product_page.click_on_proceed_to_pay).click()
