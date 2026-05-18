import pytest
from utils.helpers import get_chrome_driver

@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()