import os, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.pages.login_page import LoginPage

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

def test_login_success_selenium(driver):
    lp = LoginPage(driver)
    lp.goto(BASE_URL)
    lp.signin("demo", "P@ssw0rd")
    pre = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "result")))
    assert "access_token" in pre.text

def test_login_invalid_selenium(driver):
    lp = LoginPage(driver)
    lp.goto(BASE_URL)
    lp.signin("demo", "bad")
    pre = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "result")))
    assert "401" in pre.text
