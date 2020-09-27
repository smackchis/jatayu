class url():

    def __init__(self, driver, test_id, test_step, test_data):
        self.driver = driver
        self.test_id = test_id
        self.test_step = test_step
        self.test_data = test_data

    def Link(self):
        self.driver.get(self.test_data)

