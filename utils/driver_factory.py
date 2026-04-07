import os
import time
from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # ✅ CI environment → local Chrome
        if os.getenv("CI"):
            return webdriver.Chrome(options=options)

        # ✅ Docker environment → Selenium Grid
        for i in range(5):
            try:
                driver = webdriver.Remote(
                    command_executor="http://selenium:4444/wd/hub",
                    options=options
                )
                return driver
            except Exception:
                print(f"Retrying Selenium... {i+1}")
                time.sleep(5)

        raise Exception("Selenium not available")