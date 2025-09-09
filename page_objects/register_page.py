
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Register_page:

    Url = 'https://demowebshop.tricentis.com/register'

    # def __init__(self, driver, base_url): # Now RegisterPage inherits from BasePage and just calls .open("/register"):
    #     super().__init__(driver, base_url)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.gender_male = (By.ID, "gender-male")
        self.gender_female = (By.ID, "gender-female")
        self.first_name = (By.ID, 'FirstName')
        self.last_name = (By.ID, 'LastName')
        self.email = (By.ID, 'Email')
        self.password= (By.ID, 'Password')
        self.confirm_password = (By.ID, 'ConfirmPassword')
        self.register_button= (By.ID, 'register-button')
        self.error = (By.CSS_SELECTOR, "div.validation-summary-errors")
        self.field_error = (By.CSS_SELECTOR, "span.field-validation-error")
        self.field_errors = (By.CSS_SELECTOR, ".field-validation-error")
        self.confirm_password_error = (By.XPATH, " //span[@for='ConfirmPassword']")
        self.EMAIL_ALREADY_EXISTS= "The specified email already exists"


        self.success_message = (By.CLASS_NAME, "result")



    def load_page(self):
        self.driver.get(self.Url)


    def set_gender(self, gender="male"):
        locator=self.gender_male if gender.lower()== "male" else self.gender_female
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def set_first_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(name)

    def set_last_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys(name)

    def set_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)

    def set_password(self, password,confirm_password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.confirm_password)).send_keys(confirm_password)

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button)).click()


    def get_error(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.error)).text
        except:
            return ""
    def get_field_error(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.field_error)).text
        except:
            return ""


    def get_field_errors(self):
        # Wait until at least one field error is visible
        self.wait.until(EC.visibility_of_any_elements_located(self.field_errors))
        errors = self.driver.find_elements(*self.field_errors)
        return [e.text for e in errors if e.text.strip() != ""]

    def get_confirm_password_error(self):
        element = self.wait.until(EC.visibility_of_element_located(self.confirm_password_error))
        # wait until text is not empty
        self.wait.until(lambda driver: element.text.strip() != "")
        return element.text

    def get_success_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_message)).text
        except:
            return ""

    def get_result(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text
























