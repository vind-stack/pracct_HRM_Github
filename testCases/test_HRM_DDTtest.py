import time

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from UlitiesHRM import xlUtilities
from UlitiesHRM.customLogger import LogGen
from UlitiesHRM.readProperties import ReadConfig
from pageObjectModel.Login_HRM import LoginHRM
import allure

@allure.severity(allure.severity_level.CRITICAL)
class Test_002_DDT_HRM_Login():
    logger = LogGen.logGen()
    baseURL = ReadConfig.getAppURL()
    file = ".\\testData\\HRM_DATA.xlsx"

    @allure.severity(allure.severity_level.MINOR)
    def test_002_DDT_HRM_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("************ Test_002_DDT_HRM_Login **************")
        self.logger.info("************ test_002_DDT_HRM_Login **************")

        ddtlgn = LoginHRM(self.driver)

        rows = xlUtilities.getRowCount(self.file, "Sheet1")
        lst = []

        for r in range(2, 6):
            username = xlUtilities.readData(self.file, "Sheet1", r, 1)
            password = xlUtilities.readData(self.file, "Sheet1", r, 2)
            expresult = xlUtilities.readData(self.file, "Sheet1", r, 3)

            ddtlgn.setUsername(username)
            ddtlgn.setPassword(password)
            ddtlgn.clickLogin()
            time.sleep(5)

            actmessage = "Invalid credentials"
            expmessage = self.driver.find_element(By.TAG_NAME, "body").text

            if actmessage not in expmessage:
                if expresult == "Pass":
                    self.logger.info("************ DDT_HRM_Login is passed **************")
                    ddtlgn.clickLogout()
                    lst.append("Pass")
                elif expresult == "Fail":
                    self.logger.info("************ DDT_HRM_Login is failed **************")
                    ddtlgn.clickLogout()
                    lst.append("Fail")


            elif actmessage in expmessage:
                if expresult == "Pass":
                    self.logger.info("************ DDT_HRM_Login is failed **************")
                    lst.append("Fail")
                elif expresult == "Fail":
                    self.logger.info("************ DDT_HRM_Login is passed **************")
                    lst.append("Pass")

        if "Fail" not in lst:
            self.logger.info("************ DDT_HRM_Login is PASSED **************")
            self.driver.close()
            assert True

        else:
            self.logger.info("************ DDT_HRM_Login is failed **************")
            allure.attach(self.driver.get_screenshot_as_png(), name="testHRMDDTErrorPic", attachment_type=AttachmentType.PNG)
            ddtlgn.clickLogout()
            self.driver.close()
            self.logger.info("************ DDT_HRM_Login is COMPLETED **************")
            assert False




