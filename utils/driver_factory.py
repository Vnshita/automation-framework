import time
from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver():
        url = "http://selenium:4444/wd/hub"

        for i in range(5):  # retry 5 times
            try:
                driver = webdriver.Remote(
                    command_executor=url,
                    options=webdriver.ChromeOptions()
                )
                return driver
            except Exception:
                print(f"Retrying Selenium connection... {i+1}")
                time.sleep(5)

        raise Exception("Selenium not available")