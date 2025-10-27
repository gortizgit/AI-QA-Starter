import os
from pathlib import Path
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# --- ensure local selenium/pages package (not PyPI selenium) is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # adds .../selenium/
from pages.login_page import LoginPage  # noqa: E402

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
    pre = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "result"))
    )
    assert "access_token" in pre.text


def test_login_invalid_selenium(driver):
    lp = LoginPage(driver)
    lp.goto(BASE_URL)
    lp.signin("demo", "bad")
    pre = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "result"))
    )
    assert ("Invalid credentials" in pre.text) or ("401" in pre.text)
