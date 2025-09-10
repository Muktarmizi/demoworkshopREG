
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    for commmonly used methods
    note: through constructor it will get driver
    How to use these methods:
    1.we will use in our page classes by making Bases class as a
    perent class (put Base class in parenthise oof child class)
    2. in chile class constructor we will call Base class constructor and passs driver
    by super()
    ____
    Or
    ____
    we can create an obj of Base class in page classes
    ____
     Inherit this class in your page classes.
    - Or instantiate it directly with driver.
    """

    #generic/reuseabe methods
    #findElement
    #findElements
    #sendKeys
    #ClickOnElement
    #Dropdowns
    #Common method
    #Verify Methods
    #Browser Actions
    #Alerts
    #Frames
    #Windows
    #Waits

# Aurtor : Muktar Mizi.
# Date   : 09/10/2025


    def __init__(self, driver):
        self.driver = driver
        self.by_type = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR,
            "tag_name": By.TAG_NAME,
        }

    #-------------------findElement--------------------------------

    def find_single_element(self, locatorType, locatorValue):
        locatorType = locatorType.lower()
        return self.driver.find_element(self.by_type[locatorType], locatorValue)

    #---------------------findElements--------------------------------

    def find_list_of_elements(self, locatorType, locatorValue):
        locatorType = locatorType.lower()
        return self.driver.find_elements(self.by_type[locatorType], locatorValue)

    #----------------------ClickOnElement--------------------------------

    def click_element(self, locatorType, locatorValue):
        element = self.find_single_element(locatorType, locatorValue)
        element.click()

    # --------------------Send Keys-------------------------------------

    def send_keys(self, locatorType, locatorValue, text):
        element = self.find_single_element(locatorType, locatorValue)
        element.clear()
        element.send_keys(text)


    # ------------------Common method-------------------------------------

    def get_text(self, locatorType, locatorValue):
        element = self.find_single_element(locatorType, locatorValue)
        return element.text

    def get_attribute(self, locatorType, locatorValue, attribute_name):
        element = self.find_single_element(locatorType, locatorValue)
        return element.get_attribute(attribute_name)

    def is_element_displayed(self, locatorType, locatorValue):
        element = self.find_single_element(locatorType, locatorValue)
        return element.is_displayed()

    def is_element_enabled(self, locatorType, locatorValue):
        element = self.find_single_element(locatorType, locatorValue)
        return element.is_enabled()

    def is_element_selected(self, locatorType, locatorValue):
        element = self.find_single_element(locatorType, locatorValue)
        return element.is_selected()


    # -------------------- Verify Methods --------------------
    def verify_text(self, locatorType, locatorValue, expected_text):
        """Return True if element text matches expected"""
        element = self.find_single_element(locatorType, locatorValue)
        actual_text = element.text.strip()
        return actual_text == expected_text

    def verify_title(self, expected_title):
        """Return True if page title matches"""
        return self.driver.title.strip() == expected_title

    def verify_url_contains(self, text):
        """Return True if current URL contains given text"""
        return text in self.driver.current_url

    #------------------------------ Dropdowns---------------------------------------------

    def select_dropdown(self, locatorType, locatorValue, select_method, method_value):
        element = self.find_single_element(locatorType, locatorValue)
        select = Select(element)

        select_method = select_method.lower()
        if select_method == "index":
            select.select_by_index(int(method_value))
        elif select_method == "visible_text":
            select.select_by_visible_text(str(method_value))
        elif select_method == "value":
            select.select_by_value(str(method_value))

        # -------------------- Browser Actions --------------------

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def navigate_to_url(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

        # -------------------- Alerts --------------------

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

        # -------------------- Frames --------------------

    def switch_to_frame(self, locatorType, locatorValue):
        frame = self.find_single_element(locatorType, locatorValue)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

        # -------------------- Windows --------------------

    def switch_to_window(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

        # -------------------- Waits --------------------

    def wait_for_element_visible(self, locatorType, locatorValue, timeout=10):
        locatorType = locatorType.lower()
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located((self.by_type[locatorType], locatorValue)))
        except TimeoutException:
            return None

    def wait_for_element_clickable(self, locatorType, locatorValue, timeout=10):
        locatorType = locatorType.lower()
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.element_to_be_clickable((self.by_type[locatorType], locatorValue)))
        except TimeoutException:
            return None







