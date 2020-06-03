import test_sheet_handler

def Link(driver,test_id, test_step):
    link = test_sheet_handler.get_test_data(test_id, test_step)
    driver.get(link)

