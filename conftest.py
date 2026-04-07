import pytest
import allure
from utils.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment"
    )


@pytest.fixture(scope="function")
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


# 🔥 Allure Screenshot on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure",
                attachment_type=allure.attachment_type.PNG
            )