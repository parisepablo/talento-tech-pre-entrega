from utils.helpers import login

def test_login_accepted_credentials(driver):
    login(driver, "standard_user", "secret_sauce")
    