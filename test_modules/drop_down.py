from selenium.webdriver.support.select import Select

class SelectFromDropDown():

    def __init__(self, driver, test_id, test_step, test_data, test_variable, IdentifierType, ElementType, ElementIdentifier, Action):
        self.driver = driver
        self.test_id = test_id
        self.test_step = test_step
        self.test_data = test_data
        self.test_variable = test_variable
        self.IdentifierType = IdentifierType
        self.ElementType = ElementType
        self.ElementIdentifier = ElementIdentifier
        self.Action = Action


    def SelectElelmentType(self):

        if self.ElementType == 'id':
            self.driver.find_element_by_id(self.ElementIdentifier+f"/option[text()='{self.test_data}']").click()

        elif self.ElementType == 'xpath':
            self.driver.find_element_by_xpath(self.ElementIdentifier+f"/option[text()='{self.test_data}']").click()

        elif self.ElementType == 'name':
            self.driver.find_element_by_name(self.ElementIdentifier+f"/option[text()='{self.test_data}']").click()

