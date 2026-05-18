from utils.helpers import login
from selenium.webdriver.common.by import By 

def test_login_accepted_credentials(driver):
    login(driver, "standard_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"


def test_login_wrong_credentials(driver):
    login(driver, "locked_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/"


def test_login_empty_credentials(driver):
    login(driver, "", "")
    assert driver.current_url == "https://www.saucedemo.com/"
