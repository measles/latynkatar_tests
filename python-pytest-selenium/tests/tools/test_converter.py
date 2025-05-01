"""Tests for converter page"""

import time
from typing import Iterator

import pyperclip
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

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


def input_and_output_fields(driver: webdriver.Chrome) -> tuple[WebElement, WebElement]:
    """Finds and returns input and output fields on the converter page.

    Args:
        driver (webdriver.Chrome): Activated WebDriver from the current test esession

    Returns:
        tuple[WebElement, WebElement]: input_field, output_field
    """
    input_field = driver.find_element(by=By.ID, value="input")
    output_field = driver.find_element(by=By.ID, value="output")
    return input_field, output_field


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
    input_field, output_field = input_and_output_fields(driver)
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )

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
    input_field, output_field = input_and_output_fields(driver)
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    palatalization_check = driver.find_element(by=By.ID, value="palatalization")

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
    input_field, output_field = input_and_output_fields(driver)
    old_graphics_button = driver.find_element(
        by=By.CSS_SELECTOR, value='label[title="Старая лацінка"]'
    )
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )

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
    input_field, output_field = input_and_output_fields(driver)
    old_graphics_button = driver.find_element(
        by=By.CSS_SELECTOR, value='label[title="Старая лацінка"]'
    )
    palatalization_check = driver.find_element(by=By.ID, value="palatalization")
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    old_graphics_button.click()
    palatalization_check.click()
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ż heta szpakoŭnia? Smiech dy j hodzie!"
    )


#
# Tests on interface elements
#
def test_clean_input_field_button(driver: webdriver.Chrome):
    """Test button that should clean the input field.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field, _ = input_and_output_fields(driver)
    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    clean_input_button = driver.find_element(
        by=By.CSS_SELECTOR, value='button[title="Выдаліць тэкст"]'
    )
    time.sleep(1)

    clean_input_button.click()
    assert input_field.get_attribute("value") == ""


def test_copy_to_clipbiard_button(driver: webdriver.Chrome):
    """Test button that should copy resulting text to the clipboard.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field, _ = input_and_output_fields(driver)
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    copy_to_clipboard_button = driver.find_element(by=By.ID, value="clipboard-copy")

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    convert_button.click()
    time.sleep(1)
    copy_to_clipboard_button.click()

    assert pyperclip.paste() == "Chiba ž heta špakoŭnia? Śmiech dy j hodzie!"


#
# Tests on hotkeys
#
def test_clean_input_field_hotkey(driver: webdriver.Chrome):
    """Test hotkey that should clean the input field.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field, _ = input_and_output_fields(driver)
    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    time.sleep(1)

    chain_action = ActionChains(driver)
    chain_action.key_down(Keys.CONTROL).key_down(Keys.DELETE).key_up(
        Keys.CONTROL
    ).key_up(Keys.DELETE).perform()
    assert input_field.get_attribute("value") == ""


def test_convert_by_hotkey(driver: webdriver.Chrome):
    """Test convertation with a default settings by hotkey.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field, output_field = input_and_output_fields(driver)

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    chain_action = ActionChains(driver)
    chain_action.key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(
        Keys.CONTROL
    ).key_up(Keys.ENTER).perform()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ž heta špakoŭnia? Śmiech dy j hodzie!"
    )


def test_switch_to_old_graphics_by_hotkey(driver: webdriver.Chrome):
    """Test swithcing to old ("polish") graphics by the hotkey.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field, output_field = input_and_output_fields(driver)
    modern_graphics_button = driver.find_element(by=By.ID, value="type-modern")
    old_graphics_button = driver.find_element(by=By.ID, value="type-old")
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")

    chain_action = ActionChains(driver)
    chain_action.key_down(Keys.CONTROL).send_keys("2").key_up(Keys.CONTROL).perform()

    assert not modern_graphics_button.get_attribute("checked")
    assert old_graphics_button.get_attribute("checked")

    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ż heta szpakoŭnia? Śmiech dy j hodzie!"
    )


def test_switch_to_modern_graphics_by_hotkey(driver: webdriver.Chrome):
    """Test swithcing to modern graphics by the hotkey.

    Args:
        webdriver.Chrome: Chrome driver object
    """
    input_field, output_field = input_and_output_fields(driver)
    convert_button = driver.find_element(
        by=By.CSS_SELECTOR, value='input[title="Канвертаваць"]'
    )
    modern_graphics_button = driver.find_element(by=By.ID, value="type-modern")
    old_graphics_button = driver.find_element(by=By.ID, value="type-old")

    chain_action = ActionChains(driver)
    chain_action.key_down(Keys.CONTROL).send_keys("2").key_up(Keys.CONTROL).perform()
    chain_action.key_down(Keys.CONTROL).send_keys("1").key_up(Keys.CONTROL).perform()

    assert modern_graphics_button.get_attribute("checked")
    assert not old_graphics_button.get_attribute("checked")

    input_field.send_keys("Хіба ж гэта шпакоўня? Смех ды й годзе!")
    convert_button.click()
    time.sleep(1)

    assert (
        output_field.get_attribute("value")
        == "Chiba ž heta špakoŭnia? Śmiech dy j hodzie!"
    )
