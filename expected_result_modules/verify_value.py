import test_sheet_handler
import time

def get_elements(driver,test_id, test_step):
    expected_result_variable_list, expected_values_list = test_sheet_handler.get_expected_result(test_id,test_step)
    actual_value_list = []
    for element_num in range(0,len(expected_result_variable_list)):
        actual_value = get_actual_value(driver, expected_result_variable_list[element_num])
        actual_value_list.append(actual_value)
    test_sheet_handler.compare_actual_and_excepted_result(test_id, test_step,expected_result_variable_list, expected_values_list, actual_value_list)

def get_actual_value(driver, expected_result_variables):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(expected_result_variables)
    if ElementType == 'id':
        actual_value = CopyElementValueById(driver, IdentifierType, ElementType, ElementIdentifier, Action)

    elif ElementType == 'xpath':
        actual_value = CopyElementValueByXpath(driver, IdentifierType, ElementType, ElementIdentifier, Action)

    elif ElementType == 'name':
        actual_value = CopyElementValueByName(driver, IdentifierType, ElementType, ElementIdentifier, Action)

    return actual_value

def CopyElementValueById(driver, IdentifierType, ElementType, ElementIdentifier, Action):
    pass

def CopyElementValueByXpath(driver, IdentifierType, ElementType, ElementIdentifier, Action):
    actual_value = driver.find_element_by_xpath(ElementIdentifier).text
    return actual_value

def CopyElementValueByName(driver, IdentifierType, ElementType, ElementIdentifier, Action):
    pass

