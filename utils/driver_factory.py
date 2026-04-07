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

        # ✅ CI (GitHub Actions)
        if os.getenv("CI"):
            return webdriver.Chrome(options=options)

        # ✅ Try Docker Selenium Grid
        try:
            for i in range(3):
                try:
                    driver = webdriver.Remote(
                        command_executor="http://selenium:4444/wd/hub",
                        options=options
                    )
                    return driver
                except Exception:
                    print(f"Retry Docker Selenium... {i+1}")
                    time.sleep(3)
        except:
            pass

        # ✅ FINAL FALLBACK → Local Chrome
        print("Falling back to local Chrome...")
        return webdriver.Chrome(options=options)