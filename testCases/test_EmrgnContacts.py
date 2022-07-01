import time
import allure
import pytest
from selenium.webdriver.common.by import By
from UlitiesHRM.customLogger import LogGen
from UlitiesHRM.readProperties import ReadConfig
from pageObjectModel.Login_HRM import LoginHRM
from pageObjectModel.emrgContacts_HRM import emrgncyContacts



class Test_EmrgncyContacts():
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_003_emrgncyContacts(self, setup):
        self.logger.info("**************** Test_EmrgncyContacts *****************")
        self.logger.info("**************** test_003_emrgncyContacts *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        lgnHRM = LoginHRM(self.driver)
        lgnHRM.setUsername(self.username)
        lgnHRM.setPassword(self.password)
        lgnHRM.clickLogin()
        self.logger.info("**************** Login is successfull *****************")
        self.logger.info("**************** Writing First Emergency contacts *****************")
        emrgcntcts = emrgncyContacts(self.driver)
        emrgcntcts.clickMyinfoTab()
        emrgcntcts.clickEmrgContacts()
        emrgcntcts.clickAddButton()
        emrgcntcts.setName("Nagarajun")
        emrgcntcts.setRelationship("Grandfather")
        emrgcntcts.setHomeTelephone("45644145431612465")
        emrgcntcts.setMobileNum("8924174655")
        emrgcntcts.setWorkTelephone("08345478545410105454")
        emrgcntcts.clickSaveButton()
        time.sleep(2)
        self.logger.info("**************** Writing SECOND Emergency Contacts *****************")
        emrgcntcts.clickAddButton()
        emrgcntcts.setName("Mahesh")
        emrgcntcts.setRelationship("father")
        emrgcntcts.setHomeTelephone("4541541244685754")
        emrgcntcts.setMobileNum("9756216564")
        emrgcntcts.setWorkTelephone("947552-4165415461")
        emrgcntcts.clickSaveButton()
        self.logger.info("**************** Writing Third Emergency Contacts *****************")
        time.sleep(2)
        emrgcntcts.clickAddButton()
        emrgcntcts.setName("vinayaka")
        emrgcntcts.setRelationship("Friend")
        emrgcntcts.setHomeTelephone("4526519451421421541")
        emrgcntcts.setMobileNum("6568323532")
        emrgcntcts.setWorkTelephone("46526576-46246424641")
        emrgcntcts.clickSaveButton()
        self.logger.info("**************** Writing Fourth Emergency Contacts *****************")
        time.sleep(2)
        emrgcntcts.clickAddButton()
        emrgcntcts.setName("Modi")
        emrgcntcts.setRelationship("Senior")
        emrgcntcts.setHomeTelephone("2664526472562")
        emrgcntcts.setMobileNum("4246412462")
        emrgcntcts.setWorkTelephone("562242624-62527642")
        emrgcntcts.clickSaveButton()
        emrgcntcts.checkDeleteButtonIsDesabled()
        emrgcntcts.deleteContact("vinayaka")
        self.logger.info("**************** Emergency Contacts Is COMPLETED *****************")

        lgnHRM.clickLogout()
        self.driver.close()



















