from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Logout:
    def __init__(self, driver):
        self.driver = driver

    move_to_home = (By.XPATH, "//a[@id='nav-logo-sprites']")
    mouse_hover_on_accounts = (By.XPATH, "//a[@id='nav-link-accountList']")
    log_out = (By.XPATH, "//span[normalize-space()='Sign Out']")

    def moveToHome(self):
        self.driver.find_element(*Logout.move_to_home).click()

    def mouseHoverOnAccount(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*Logout.mouse_hover_on_accounts)).perform()

    def logOut(self):
        self.driver.find_element(*Logout.log_out).click()
