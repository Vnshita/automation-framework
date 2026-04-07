import pytest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


def test_login(driver, request):

    config = ConfigReader.read_config(request)
    base_url = config["environments"][config["env"]]

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    assert "Secure Area" in driver.page_source