from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    choose_address = (By.XPATH, "//div[@class='a-row address-row list-address-selected']")

    # popup = (By.XPATH, "")

    price = (By.XPATH, "//td[@class='a-color-price a-size-medium a-text-right grand-total-price aok-nowrap "
                       "a-text-bold a-nowrap']")

    select_address = (By.XPATH, "//input[@data-testid='Address_selectShipToThisAddress']")

    select_payment_option = (By.XPATH, "(//div[@class='a-row a-spacing-base'])[2]")



    def chooseAddress(self):
        self.driver.find_element(*Checkout.choose_address).click()

    def itemPrice(self):
        self.driver.find_element(*Checkout.price)

    def selectAddress(self):
        self.driver.find_element(*Checkout.select_address).click()

    def selectPaymentOption(self):
        self.driver.find_element(*Checkout.select_payment_option).click()