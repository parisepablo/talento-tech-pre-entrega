from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_chrome_driver():
    service = Service(ChromeDriverManager().install())
    # Disable password manager to prevent pop-ups during tests
    options = Options()
    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def login(driver, username, password):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    driver.find_element(By.ID, "login-button").click()