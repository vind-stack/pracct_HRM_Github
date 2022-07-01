import time
from selenium.webdriver.common.by import By

class LoginHRM:

    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login_id = "btnLogin"
    linktext_namelogout_xpath = "//a[@id='welcome']"
    linktext_logout_lnktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.linktext_namelogout_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, self.linktext_logout_lnktext).click()


