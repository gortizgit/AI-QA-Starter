from playwright.sync_api import expect
from qa.pages.login_page import LoginPage  # ajusta el import si tu ruta difiere


def test_login_success(page):
    page.set_default_timeout(5000)
    lp = LoginPage(page)
    lp.goto()
    lp.signin("demo", "P@ssw0rd")
    expect(lp.result).to_be_visible()
    txt = lp.result.inner_text()
    assert "access_token" in txt


def test_login_invalid(page):
    page.set_default_timeout(5000)
    lp = LoginPage(page)
    lp.goto()
    lp.signin("demo", "bad")
    expect(lp.result).to_be_visible()
    txt = lp.result.inner_text()
    assert ("Invalid credentials" in txt) or ("401" in txt)
