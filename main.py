from selenium import webdriver
import sys
import time
from datetime import datetime
import test_sheet
from test_modules import click, enter_value, login


def run_tests(test_id):
    row_no = 3
    while row_no <= test_sheet.ws.max_row:
        if str(test_sheet.ws.cell(row=row_no, column=1).value).strip() == str(test_id):
            test_module = str(test_sheet.ws.cell(row=row_no, column=2).value).strip()
            #test_method = str(test_sheet.ws.cell(row=row_no, column=3).value).strip()
            test_variable = str(test_sheet.ws.cell(row=row_no, column=3).value).strip()
            test_step = str(test_sheet.ws.cell(row=row_no, column=6).value).strip()
            try:
                if test_variable != None:
                    print(datetime.now(),"TestModule:",test_module, "\t TestMethod:", test_variable, "\t test_id:", test_id, "\t test_step:", test_step)
                    if test_module == 'login':
                        time.sleep(3)
                        getattr(login, test_variable)(driver, test_id, test_step)
                    if test_module == 'enter_value':
                        time.sleep(1)
                        getattr(enter_value, 'SelectElelmentType')(driver, test_id, test_step, test_variable)
                    if test_module == 'click':
                        time.sleep(1)
                        getattr(click, 'SelectElelmentType')(driver, test_id, test_step, test_variable)

            except:
                print(sys.exc_info())
                exception = sys.exc_info()[0]
                print(exception)
                test_sheet.AutomationException(test_id,test_step,str(exception))
            finally:
                pass
        row_no = row_no + 1

driver = webdriver.Chrome(executable_path=r"C:\TM\jatayu\etc\chromedriver.exe")
driver.maximize_window()
test_id, row = 1,3

while test_id <= int(test_sheet.total_cases):
    run_tests(test_id)
    test_id = test_id + 1

#driver.close()
