from features import evaluations
from selenium.webdriver.common.keys import Keys

class SendValue():

    def __init__(self,driver,test_id, test_step, test_data, test_variable, IdentifierType, ElementType, ElementIdentifier, Action):
        self.driver = driver
        self.test_id = test_id
        self.test_step = test_step
        self.test_data = test_data
        self.test_variable = test_variable
        self.IdentifierType = IdentifierType
        self.ElementType = ElementType
        self.ElementIdentifier = ElementIdentifier
        self.Action = Action

    def SendKeysByElement(self):
        if self.test_data.startswith('fx=('):
            value = evaluations.evalute_function(self.driver,self.test_data)
        else:
            value = self.test_data

        if self.ElementType == 'id':
            self.driver.find_element_by_id(self.ElementIdentifier).send_keys(Keys.CONTROL + "a")
            self.driver.find_element_by_id(self.ElementIdentifier).send_keys(Keys.DELETE)
            self.driver.find_element_by_id(self.ElementIdentifier).send_keys(value)

        elif self.ElementType == 'xpath':
            self.driver.find_element_by_xpath(self.ElementIdentifier).send_keys(Keys.CONTROL + "a");
            self.driver.find_element_by_xpath(self.ElementIdentifier).send_keys(Keys.DELETE);
            self.driver.find_element_by_xpath(self.ElementIdentifier).send_keys(value)

        elif self.ElementType == 'name':
            self.driver.find_element_by_name(self.ElementIdentifier).send_keys(Keys.CONTROL + "a");
            self.driver.find_element_by_name(self.ElementIdentifier).send_keys(Keys.DELETE);
            self.driver.find_element_by_name(self.ElementIdentifier).send_keys(value)



