import test_sheet_handler
import time

def SelectElelmentType(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)

    if ElementType == 'id':
        ClickElementById(driver,test_id, test_step,test_variable)

    elif ElementType == 'xpath':
        ClickElementByXpath(driver,test_id, test_step,test_variable)

    elif ElementType == 'name':
        ClickElementByName(driver,test_id, test_step,test_variable)

def ClickElementById(driver,test_id, test_step,test_variable):
    #time.sleep(2)
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_id(ElementIdentifier).click()

def ClickElementByXpath(driver,test_id, test_step,test_variable):
    #time.sleep(2)
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_xpath(ElementIdentifier).click()

def ClickElementByName(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(test_variable)
    driver.find_element_by_name(ElementIdentifier).click()

