from qa.pages.login_page import LoginPage
from playwright.sync_api import expect

BASE_URL = "http://127.0.0.1:8000"

def test_login_success(page):
    page.set_default_timeout(5000)
    lp = LoginPage(page)
    lp.goto()
    lp.signin("demo", "P@ssw0rd")
    expect(lp.result).to_contain_text("access_token")

def test_login_invalid(page):
    page.set_default_timeout(5000)
    lp = LoginPage(page)
    lp.goto()
    lp.signin("demo", "bad")
    expect(lp.result).to_contain_text("401")
