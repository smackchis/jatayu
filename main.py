from selenium import webdriver
import openpyxl
import importlib
import os
import sys
import time
import globals
from datetime import datetime
import test_sheet_handler
from importlib import reload
from test_modules import drop_down, click, enter_value, get_url
from expected_result_modules import verify_value

def run_tests(test_id):
    row_no = 3
    while row_no <= test_sheet_handler.ws.max_row:
        if str(test_sheet_handler.ws.cell(row=row_no, column=1).value).strip() == str(test_id):
            test_module = str(test_sheet_handler.ws.cell(row=row_no, column=2).value).strip()
            test_variable = str(test_sheet_handler.ws.cell(row=row_no, column=3).value).strip()
            test_step = str(test_sheet_handler.ws.cell(row=row_no, column=6).value).strip()
            expected_result_module = str(test_sheet_handler.ws.cell(row=row_no, column=8).value)
            if test_sheet_handler.ws.cell(row=row_no, column=8).value != None:
                expected_result_module = (str(test_sheet_handler.ws.cell(row=row_no, column=8).value).strip().split('::')[1])[1:]

            try:
                if test_variable != None:
                    print(datetime.now(),"TestModule:",test_module, "\t TestMethod:", test_variable, "\t test_id:", test_id, "\t test_step:", test_step)
                    if test_module == 'get_url':
                        time.sleep(10)
                        getattr(get_url, 'Link')(driver, test_id, test_step)
                    if test_module == 'enter_value':
                        time.sleep(test_sheet_handler.WaitTime)
                        getattr(enter_value, 'SelectElelmentType')(driver, test_id, test_step, test_variable)
                    if test_module == 'click':
                        time.sleep(test_sheet_handler.WaitTime)
                        getattr(click, 'SelectElelmentType')(driver, test_id, test_step, test_variable)
                    if test_module == 'drop_down':
                        time.sleep(test_sheet_handler.WaitTime)
                        getattr(drop_down, 'SelectElelmentType')(driver, test_id, test_step, test_variable)

                    if expected_result_module == 'verify_value':
                        time.sleep(test_sheet_handler.WaitTime)
                        getattr(verify_value, 'get_elements')(driver, test_id, test_step)
                    if expected_result_module == 'None':
                        test_sheet_handler.compare_actual_and_excepted_result(test_id, test_step, '', '', '')

            except:
                print(sys.exc_info())
                exception = sys.exc_info()[0]
                print(exception)
                test_sheet_handler.AutomationException(test_id, test_step, str(exception))
            finally:
                pass
        row_no = row_no + 1


driver = webdriver.Chrome(executable_path=globals.driverpath)
driver.maximize_window()

for prow in range(2,test_sheet_handler.ProjectsWS.max_row+1):
    globals.project  = str(test_sheet_handler.ProjectsWS.cell(row=prow,column=1).value).strip()
    if globals.project != 'None' and (str(test_sheet_handler.ProjectsWS.cell(row=prow,column=2).value).strip()).lower() == 'yes':
        TestSuitPath = globals.ProjectPath + "\\test_suite\\" + globals.project + "\\"
        for TestSuits in os.listdir(TestSuitPath):
            if TestSuits.endswith(".xlsm") and "~$" not in TestSuits:
                globals.test_suite_path = os.path.join(TestSuitPath, TestSuits)
                globals.test_sheet = TestSuits[2:-5] + '_TestCase'
                print(globals.test_suite_path, globals.test_sheet)
                reload(test_sheet_handler)
                test_id, row = 1,3
                while test_id <= int(test_sheet_handler.total_cases):
                    run_tests(test_id)
                    test_id = test_id + 1

#driver.close()
