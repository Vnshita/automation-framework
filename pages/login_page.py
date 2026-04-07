from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.flash.success")

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def wait_for_success(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )