import subprocess
import sys
import time

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True)
def app_server():
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--port", "8000", "--reload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(1.5)
    yield
    proc.terminate()


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(base_url="http://127.0.0.1:8000")
        yield context
        browser.close()


@pytest.fixture()
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()
