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


#
# Test on page view
#
def test_page_title(driver: webdriver.Chrome):
    """Test for title of a converter page.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    assert driver.title == "Łatynkatar"


#
# Tests on text convertation
#
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

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ž heta špakoŭnia? Śmiech dy j hodzie!"
    )


def test_convert_without_palatalization(driver: webdriver.Chrome):
    """Test convertation without palatalization.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field = driver.find_element(by=By.ID, value="input")
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    palatalization_check = driver.find_element(by=By.ID, value="palatalization")
    output_field = driver.find_element(by=By.ID, value="output")

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    palatalization_check.click()
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ž heta špakoŭnia? Smiech dy j hodzie!"
    )


def test_convert_to_old_graphics(driver: webdriver.Chrome):
    """Test convertation to an old graphics.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field = driver.find_element(by=By.ID, value="input")
    old_graphics_button = driver.find_element(
        by=By.CSS_SELECTOR, value='label[title="Старая лацінка"]'
    )
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    output_field = driver.find_element(by=By.ID, value="output")

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    old_graphics_button.click()
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ż heta szpakoŭnia? Śmiech dy j hodzie!"
    )


def test_convert_to_old_graphics_without_palatalization(driver: webdriver.Chrome):
    """Test convertation to an old graphics without palatalization.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field = driver.find_element(by=By.ID, value="input")
    old_graphics_button = driver.find_element(
        by=By.CSS_SELECTOR, value='label[title="Старая лацінка"]'
    )
    palatalization_check = driver.find_element(by=By.ID, value="palatalization")
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    output_field = driver.find_element(by=By.ID, value="output")

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    old_graphics_button.click()
    palatalization_check.click()
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ż heta szpakoŭnia? Smiech dy j hodzie!"
    )
