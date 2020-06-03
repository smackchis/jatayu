import test_sheet

def SelectElelmentType(driver,test_id, test_step,test_variable):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet.get_element_repo(test_variable)

    if ElementType == 'id':
        EntervalueByElementId(driver,test_id, test_step,test_variable)

    elif ElementType == 'xpath':
        EntervalueByElementXpath(driver,test_id, test_step,test_variable)

def EntervalueByElementId(driver,test_id, test_step,test_variable):
    value = test_sheet.get_test_data(test_id, test_step)
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet.get_element_repo(test_variable)
    driver.find_element_by_id(ElementIdentifier).send_keys(value)

def EntervalueByElementXpath(driver,test_id, test_step,test_variable):
    value = test_sheet.get_test_data(test_id, test_step)
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet.get_element_repo(test_variable)
    driver.find_element_by_xpath(ElementIdentifier).send_keys(value)