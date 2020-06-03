import test_sheet

def Link(driver,test_id, test_step):
    link = test_sheet.get_test_data(test_id, test_step)
    driver.get(link)

