import os, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from applitools.selenium import Eyes, BatchInfo, Target

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
    eyes.configure.set_batch(BatchInfo("Local Dev"))
    yield eyes

def test_visual_login_page(driver, eyes):
    eyes.open(driver=driver, app_name="AI-QA-Starter", test_name="Login Page Visual", viewport_size={"width": 800, "height": 600})
    driver.get(BASE_URL + "/")
    eyes.check(Target.window().fully())
    eyes.close_async()
