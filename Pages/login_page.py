from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    click_login = (By.XPATH, "//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner'][normalize-space("
                             ")='Sign in']")
    email = (By.XPATH, "//input[@id='ap_email']")
    click_continue = (By.XPATH, "//input[@id='continue']")
    password = (By.XPATH, "//input[@id='ap_password']")
    click_submit = (By.XPATH, "//input[@id='signInSubmit']")

    def clickLogin(self):
        self.driver.find_element(*Login.click_login).click()

    def enterEmail(self, username):
        self.driver.find_element(*Login.email).send_keys(username)

    def clickContinue(self):
        self.driver.find_element(*Login.click_continue).click()

    def enterPass(self, password):
        self.driver.find_element(*Login.password).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element(*Login.click_submit).click()
