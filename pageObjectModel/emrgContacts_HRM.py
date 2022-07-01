import time
from selenium.webdriver.common.by import By

class emrgncyContacts():

    linktext_Myinfo_linktext = "My Info"
    linktext_EmrgncyContacts_linktext = "Emergency Contacts"
    button_Add_xpath = "//input[@id='btnAddContact']"
    textbox_Name_xpath = "//input[@id='emgcontacts_name']"
    textbox_Relation_xpath = "//input[@id='emgcontacts_relationship']"
    textbox_Hometelephone_xpath = "//input[@id='emgcontacts_homePhone']"
    textbox_Mobile_xpath = "//input[@id='emgcontacts_mobilePhone']"
    textbox_Workphone_xpath = "//input[@id='emgcontacts_workPhone']"
    button_Save_xpath = "//input[@id='btnSaveEContact']"
    button_Delete_id = "delContactsBtn"
    table_allrows_xpath = "//table[@id='emgcontact_list']/tbody/tr"
    table_allcolumns_xpath = "//table[@id='emgcontact_list']//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickMyinfoTab(self):
        self.driver.find_element(By.LINK_TEXT, self.linktext_Myinfo_linktext).click()

    def clickEmrgContacts(self):
        self.driver.find_element(By.LINK_TEXT, self.linktext_EmrgncyContacts_linktext).click()

    def clickAddButton(self):
        self.driver.find_element(By.XPATH, self.button_Add_xpath).click()

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.textbox_Name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Name_xpath).send_keys(name)

    def setRelationship(self, relationship):
        self.driver.find_element(By.XPATH, self.textbox_Relation_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Relation_xpath).send_keys(relationship)

    def setHomeTelephone(self, hometelenum):
        self.driver.find_element(By.XPATH, self.textbox_Hometelephone_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Hometelephone_xpath).send_keys(hometelenum)

    def setMobileNum(self, mobilenum):
        self.driver.find_element(By.XPATH, self.textbox_Mobile_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Mobile_xpath).send_keys(mobilenum)

    def setWorkTelephone(self, worktelenum):
        self.driver.find_element(By.XPATH, self.textbox_Workphone_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Workphone_xpath).send_keys(worktelenum)

    def clickSaveButton(self):
        message = self.driver.find_element(By.TAG_NAME, "body").text
        if "Allows numbers" in message:
            raise Exception("Please Provide Only the Numbers and not the alphabets")
        else:
            self.driver.find_element(By.XPATH, self.button_Save_xpath).click()

    def checkDeleteButtonIsDesabled(self):
        delete = self.driver.find_element(By.ID, self.button_Delete_id)
        return delete.is_enabled()

    def countAllRows(self):
        allrows = len(self.driver.find_elements(By.XPATH, self.table_allrows_xpath))
        print(allrows)
        return allrows

    def deleteContact(self, contactname):
        allrows = len(self.driver.find_elements(By.XPATH, self.table_allrows_xpath))
        for r in range(2, allrows+1):
            name = self.driver.find_element(By.XPATH, "//table[@id='emgcontact_list']/tbody/tr["+str(r)+"]/td[2]").text
            if name == contactname:
                self.driver.find_element(By.XPATH, "//table[@id='emgcontact_list']/tbody/tr["+str(r)+"]/td[1]").click()
                time.sleep(5)
                self.driver.find_element(By.ID, self.button_Delete_id).click()

    def deleteMultipleContacts(self):
        allrows = len(self.driver.find_elements(By.XPATH, self.table_allrows_xpath))
        for r in range(2, allrows+1):
            self.driver.find_element(By.XPATH, "//table[@id='emgcontact_list']/tbody/tr["+str(r)+"]/td[1]").click()
            # time.sleep(5)
            # self.driver.find_element(By.ID, self.button_Delete_id).click()



