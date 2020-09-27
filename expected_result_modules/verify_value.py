import test_sheet_handler

class CompareResults():

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
        self.expected_result_variable_list, self.expected_values_list = test_sheet_handler.get_expected_result(test_id, test_step)

    def GetTestStatus(self):
        actual_value_list = []
        #print(self.expected_result_variable_list)
        for element_num in range(0,len(self.expected_result_variable_list)):
            #print(self.expected_result_variable_list[element_num])
            actual_value_posibilities_list = []
            for n in range(0,len(list(self.expected_result_variable_list[element_num]))):
                actual_value_posibilities = get_actual_value(self.driver, list(self.expected_result_variable_list[element_num])[n])
                actual_value_posibilities_list.append(actual_value_posibilities)
            actual_value_list.append(actual_value_posibilities_list)
        test_sheet_handler.compare_actual_and_excepted_result(self.test_id, self.test_step, self.expected_result_variable_list, self.expected_values_list, actual_value_list)

def get_actual_value(driver, expected_result_variables):
    IdentifierType, ElementType, ElementIdentifier, Action = test_sheet_handler.get_element_repo(expected_result_variables)

    if ElementType == 'id':
        if Action.split('=')[0] == 'get_attribute':
            actual_value = driver.find_element_by_id(ElementIdentifier).get_attribute(Action.split('=')[1])
        if Action == 'copy_text':
            actual_value = driver.find_element_by_id(ElementIdentifier).text

    elif ElementType == 'xpath':
        if Action.split('=')[0] == 'get_attribute':
            actual_value = driver.find_element_by_xpath(ElementIdentifier).get_attribute(Action.split('=')[1])
        if Action == 'copy_text':
            actual_value = driver.find_element_by_xpath(ElementIdentifier).text

    elif ElementType == 'name':
        if Action.split('=')[0] == 'get_attribute':
            actual_value = driver.find_element_by_name(ElementIdentifier).get_attribute(Action.split('=')[1])
        if Action == 'copy_text':
            actual_value = driver.find_element_by_name(ElementIdentifier).text
    #print('actual value =', text_copied)
    return actual_value

