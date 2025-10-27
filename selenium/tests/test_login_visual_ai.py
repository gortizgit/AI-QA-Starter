import os
from pathlib import Path
import sys

import pytest
from applitools.selenium import BatchInfo, Eyes, Target
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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


@pytest.fixture
def eyes():
    eyes = Eyes()
    eyes.configure.set_app_name("AI-QA-Starter").set_test_name("Login Page Visual")
    eyes.configure.set_batch(BatchInfo("CI"))
    yield eyes


def test_visual_login_page(driver, eyes):
    # use the page object to keep selectors consistent (optional)
    lp = LoginPage(driver)
    lp.goto(BASE_URL)

    eyes.open(
        driver=driver,
        app_name="AI-QA-Starter",
        test_name="Login Page Visual",
        viewport_size={"width": 1000, "height": 700},
    )
    eyes.check(Target.window().fully())
    eyes.close_async()
