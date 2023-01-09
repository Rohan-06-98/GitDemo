import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:
    def verify_link_presence(self, path, timeout=10):
        """

        :param path:
        :param timeout:
        :return:
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.presence_of_element_located(path))

    def verify_clickable(self, path, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.element_to_be_clickable(path))

    def Scroll_page(self, value):
        self.driver.execute_script(value)