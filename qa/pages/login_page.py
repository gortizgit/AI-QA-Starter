from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.submit   = page.get_by_role("button", name="Sign in")
        self.result   = page.locator("#result")

    def goto(self):
        self.page.goto("/")

    def signin(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()
