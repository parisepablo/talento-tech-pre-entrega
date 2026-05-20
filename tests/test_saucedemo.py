from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


## Cart test cases
def test_add_product_to_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)
    inventory_item_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']"))).text
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-test, 'add-to-cart')]"))).click
    # Validate that cart badge shows 1 item
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))).text == "1"
    # Validate product is added to cart
    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
    cart_item_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']"))).text
    assert cart_item_name == inventory_item_name