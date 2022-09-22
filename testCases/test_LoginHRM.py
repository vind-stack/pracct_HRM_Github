import time
import allure
import pytest
from allure_commons.types import AttachmentType
from UlitiesHRM.customLogger import LogGen
from UlitiesHRM.readProperties import ReadConfig
from pageObjectModel.Login_HRM import LoginHRM

@allure.severity(allure.severity_level.NORMAL)
class Test_01_HRMLogin():
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @allure.severity(allure.severity_level.MINOR)
    def test_001_LoginHRM_title(self, setup):
        self.logger.info("***************** HRMLogin_title_Check ********************")
        self.logger.info("***************** test_001_LoginHRMTitle ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        expTitle = "OrangeHRM"
        actTitle = self.driver.title
        print(actTitle)
        if expTitle == actTitle:
            assert True
            self.driver.close()
            self.logger.info("***************** HRMLogin is successfull ********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "HRMTitleError.jpg")
            self.logger.error("***************** HRMLogin is unsuccessfull ********************")
            self.driver.close()
            assert False




    @allure.severity(allure.severity_level.CRITICAL)
    def test_002_LoginHRM(self, setup):
        self.logger.info("***************** HRMLogin ********************")
        self.logger.info("***************** test_002_LoginHRM ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("***************** Login into HRM ********************")
        self.lghrm = LoginHRM(self.driver)
        self.lghrm.setUsername(self.username)
        self.lghrm.setPassword(self.password)
        self.lghrm.clickLogin()
        self.logger.info("***************** HRMLogin is successfull ********************")
        message = self.driver.find_element(By.TAG_NAME,"body").text
        print(message)

        if "Personal Details" in message:
            self.logger.info("***************** HRMLogin Myinfo Page ********************")
            time.sleep(5)
            self.lghrm.clickLogout()
            self.driver.close()
            assert True == True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="allureErrorPic", attachment_type=AttachmentType.PNG)
            # self.driver.save_screenshot(".\\Screenshots\\" + "pageError.png")
            self.logger.error("***************** HRM Page Error ********************")
            #time.sleep(5)
            self.lghrm.clickLogout()
            self.logger.error("***************** HRM Failed ********************")
            self.driver.close()
            assert True == False
