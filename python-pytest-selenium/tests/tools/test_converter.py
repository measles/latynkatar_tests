from selenium import webdriver
from pytest import fixture
from lib.config import BASE_URL

@fixture(name="driver")
def get_ready_to_test_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver
    
    driver.quit()
    
    
def test_page_title(driver):
    assert driver.title == "Łatynkatar"    

