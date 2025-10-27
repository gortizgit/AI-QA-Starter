from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto(self, base_url: str):
        self.driver.get(base_url + "/")

    def signin(self, user: str, pwd: str):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
