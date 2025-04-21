"""Tests for converter page"""

from typing import Generator

from pytest import fixture
from selenium import webdriver

from lib.config import BASE_URL


@fixture(name="driver")
def get_ready_to_test_driver() -> Generator[webdriver.Chrome]:
    """Generates redy to application driver object and opens converter page.
        After test execution properly closes the driver session.

    Yields:
        Any: Ready for execution  Chrome driver object
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


def test_page_title(driver: webdriver.Chrome):
    """Test for title of a converter page.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    assert driver.title == "Łatynkatar"
