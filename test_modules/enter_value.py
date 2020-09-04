import test_sheet_handler
from selenium.webdriver.common.keys import Keys
import time

def SelectElelmentType(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)

    if ElementType == 'id':
        EntervalueByElementId(driver,test_id, test_step,test_variable,IdentifierType, ElementType, ElementIdentifier, Action)

    elif ElementType == 'xpath':
        EntervalueByElementXpath(driver,test_id, test_step,test_variable,IdentifierType, ElementType, ElementIdentifier, Action)

    elif ElementType == 'name':
        EntervalueByElementName(driver,test_id, test_step,test_variable,IdentifierType, ElementType, ElementIdentifier, Action)

def EntervalueByElementId(driver,test_id, test_step,test_variable, IdentifierType, ElementType, ElementIdentifier, Action):
    #time.sleep(2)
    value = test_sheet_handler.get_test_data(test_id, test_step)
    #IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_id(ElementIdentifier).send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id(ElementIdentifier).send_keys(Keys.DELETE)
    driver.find_element_by_id(ElementIdentifier).send_keys(value)

def EntervalueByElementXpath(driver,test_id, test_step,test_variable,IdentifierType, ElementType, ElementIdentifier, Action):
    #time.sleep(2)
    value = test_sheet_handler.get_test_data(test_id, test_step)
    #IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_xpath(ElementIdentifier).send_keys(Keys.CONTROL + "a");
    driver.find_element_by_xpath(ElementIdentifier).send_keys(Keys.DELETE);
    driver.find_element_by_xpath(ElementIdentifier).send_keys(value)

def EntervalueByElementName(driver,test_id, test_step,test_variable,IdentifierType, ElementType, ElementIdentifier, Action):
    value = test_sheet_handler.get_test_data(test_id, test_step)
    #IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_name(ElementIdentifier).send_keys(value)
