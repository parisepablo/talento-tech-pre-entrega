from utils.helpers import login
from selenium.webdriver.common.by import By 

## Login test cases
def test_login_accepted_credentials(driver):
    login(driver, "standard_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"


def test_login_wrong_credentials(driver):
    login(driver, "wrong_user", "wrong_password")
    assert driver.current_url == "https://www.saucedemo.com/"


def test_login_empty_credentials(driver):
    login(driver, "", "")
    assert driver.current_url == "https://www.saucedemo.com/"


## Catalog test cases
def test_catalog_products_displayed(driver):
    login(driver, "standard_user", "secret_sauce")
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    inventory_items = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(inventory_items) > 0
    assert inventory_items[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text == "Sauce Labs Backpack"
    assert inventory_items[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text == "$29.99"
    assert inventory_items[0].find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").is_displayed()