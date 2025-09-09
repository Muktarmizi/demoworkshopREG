class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, path=""):
        """Open any page by appending path to base_url"""
        url = f"{self.base_url}{path}"
        self.driver.get(url)
