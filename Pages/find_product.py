from selenium.webdriver.common.by import By


class Find_product:

    def __init__(self, driver):
        self.driver = driver

    enter_item_name = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    submit = (By.XPATH, "//input[@id='nav-search-submit-button']")
    select_item = (By.XPATH, "//img[@alt='Sponsored Ad - Apple iPhone 12 (64GB) - (Product) RED']")

    def item_name(self):
        self.driver.find_element(*Find_product.enter_item_name).send_keys("Iphone 12")

    def submit_name(self):
        self.driver.find_element(*Find_product.submit).click()

    def select_prod(self):
        self.driver.find_element(*Find_product.select_item).click()
