import test_sheet

def SelectElelmentType(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet.get_element_repo(test_variable)

    if ElementType == 'id':
        ClickElementById(driver,test_id, test_step,test_variable)

    elif ElementType == 'xpath':
        ClickElementByXpath(driver,test_id, test_step,test_variable)

def ClickElementById(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet.get_element_repo(test_variable)
    driver.find_element_by_id(ElementIdentifier).click()

def ClickElementByXpath(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet.get_element_repo(test_variable)
    driver.find_element_by_xpath(ElementIdentifier).click()


