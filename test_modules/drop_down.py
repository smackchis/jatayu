import test_sheet_handler
from selenium.webdriver.support.select import Select
import time

def SelectElelmentType(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)

    if ElementType == 'id':
        SelectElementById(driver,test_id, test_step,test_variable)

    elif ElementType == 'xpath':
        SelectElementByXpath(driver,test_id, test_step,test_variable)

    elif ElementType == 'name':
        SelectElementByName(driver,test_id, test_step,test_variable)


def SelectElementById(driver,test_id, test_step,test_variable):
    pass
    #IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    #driver.find_element_by_id("//select[@name='element_name']/option[text()='option_text']").click(
    #Select(driver.find_element_by_id(ElementIdentifier)).first_selected_option.text

def SelectElementByXpath(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_xpath(ElementIdentifier+f"/option[text()='{test_sheet_handler.get_test_data(test_id, test_step)}']").click()

def SelectElementByName(driver,test_id, test_step,test_variable):
    pass
