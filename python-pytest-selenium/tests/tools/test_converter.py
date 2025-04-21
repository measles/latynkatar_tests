"""Tests for converter page"""

import time
from typing import Iterator

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By

from lib.config import BASE_URL


@fixture(name="driver")
def get_ready_to_test_driver() -> Iterator[webdriver.Chrome]:
    """Generates redy to application driver object and opens converter page.
        After test execution properly closes the driver session.

    Yields:
        Any: Ready for execution  Chrome driver object
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


def test_page_title(driver: webdriver.Chrome):
    """Test for title of a converter page.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    assert driver.title == "Łatynkatar"


def test_convert_default(driver: webdriver.Chrome):
    """Test convertation with a default settings.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field = driver.find_element(by=By.ID, value="input")
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    output_field = driver.find_element(by=By.ID, value="output")

    input_field.send_keys(
        "Варажылі важаняткі ў падножжацёмнай вежы, бо хацелі важаняткі адшукаць у лесе ежы."
    )
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Varažyli važaniatki ŭ padnožžaciomnaj viežy, bo chacieli važaniatki adšukać u lesie ježy."
    )
