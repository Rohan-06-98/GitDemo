import time

from Pages.checkout_page import Checkout
# from Pages.Home_page import HomePage
from Pages.find_product import Find_product
from Pages.logout_page import Logout
from Pages.product_page import Product_page
from utilities.Base_class import BaseClass
from Pages.login_page import Login


class TestMain(BaseClass):
    def test_e2e(self, get_username, get_password):
        login = Login(self.driver)
        self.verify_link_presence(login.click_login)
        login.clickLogin()
        login.enterEmail(get_username)
        print(get_username)
        self.verify_link_presence(login.click_continue)
        login.clickContinue()
        login.enterPass(get_password)
        self.verify_link_presence(login.click_submit)
        login.clickSubmit()
        time.sleep(6)

        product = Find_product(self.driver)
        product.item_name()
        self.verify_link_presence(product.submit)
        product.submit_name()
        # time.sleep(6)
        self.Scroll_page("window.scrollBy(0,200)")
        self.verify_link_presence(product.select_item)
        product.select_prod()
        time.sleep(6)

        windowsOpen = self.driver.window_handles
        self.driver.switch_to.window(windowsOpen[1])
        self.Scroll_page("window.scrollBy(0,300)")

        buy_product = Product_page(self.driver)
        self.verify_link_presence(buy_product.add_to_cart)
        buy_product.addToCart()
        self.verify_link_presence(buy_product.clik_to_cut_popup)
        buy_product.cutPopup()
        self.verify_link_presence(buy_product.go_to_cart)
        time.sleep(3)
        buy_product.goToCart()
        self.verify_link_presence(buy_product.click_on_proceed_to_pay)
        buy_product.clickOnProceedToBuy()

        checkout = Checkout(self.driver)

        # print(checkout.itemPrice()).text)
        self.verify_link_presence(checkout.select_address)
        checkout.selectAddress()
        self.verify_link_presence(checkout.select_payment_option)
        checkout.selectPaymentOption()

        self.driver.switch_to.window(windowsOpen[0])
        self.Scroll_page("window.scrollBy(0,-300)")

        logout = Logout(self.driver)
        self.verify_link_presence(logout.move_to_home)
        logout.moveToHome()
        logout.mouseHoverOnAccount()
        self.verify_link_presence(logout.log_out)
        logout.logOut()

        self.driver.get_screenshot_as_file("sign_out.png")

        time.sleep(6)

# here the Amazon project is completed.
