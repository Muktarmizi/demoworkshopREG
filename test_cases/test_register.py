import pytest
from selenium import webdriver
import time
from page_objects.register_page import Register_page
from utils.logger import get_logger


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

logger = get_logger(__name__)
def test(driver):
    register = Register_page(driver)




#--------------------------------------Happy Path------------------------------------------------------#

#need to check the user is a already is used by loggin.
def test_register_page(driver):
    logger.info(f"Testing register page")
    register = Register_page(driver)
    register.load_page()
    register.set_gender("male")
    time.sleep(3)
    register.set_first_name("mizi")
    time.sleep(3)
    register.set_last_name("muktar")
    time.sleep(3)
    register.set_email("dem_12345678@gmail.com") #keep adding number on email for Succesfully Registered.
    time.sleep(3)
    register.set_password("123456","123456")
    time.sleep(3)
    register.submit()
    time.sleep(3)
    if "Your registration completed" in register.get_success_message():
        print(" Registered successfully")

    else:
        register.driver.get_screenshot_as_file(".//screenshots//test_register_screenshot.png")
        error = register.get_error()
        assert  "The specified email already exists" in error
        print(" Registration failed The specified email already exists")


    #result_text =register.get_result()
    #print(result_text)
    #assert "Your registration completed" in result_text


    #------------------------------Negative Tests----------------------------------------------------#




def test_001_registration_missing_required_fields(driver):
        logger.info(f"Testing register page with missing required fields")
        register = Register_page(driver)
        register.load_page()
        register.submit()  # directly submit without filling anything
        time.sleep(3)

        register.driver.get_screenshot_as_file(".//screenshots//test_001_missing_required_fields.png")
        errors = register.get_field_errors()

        assert "First name is required." in errors
        assert "Last name is required." in errors
        assert "Email is required." in errors
        assert "Password is required." in errors
        assert "Password is required." in errors # confirm password
        print(" Registration failed for missing required fields")



def test_002_register_password_mismatch(driver):
            logger.info(f"Testing register page with password mismatch")
            register = Register_page(driver)
            register.load_page()
            register.set_gender("male")
            register.set_first_name("muktar")
            register.set_last_name("mizi")
            register.set_email("mizimuktar0@gmail.com")
            register.set_password("Enthrall", "Enthrall12")  # mismatch
            register.submit()

            register.driver.get_screenshot_as_file(".//screenshots//test_002_password_mismatch.png")
            error = register.get_confirm_password_error()


            assert "The password and confirmation password do not match." in error
            print(" Registration failed Password Mismatch")


def test_003_registration_existing_email(driver):
        logger.info(f"Testing register page with existing email")
        register = Register_page(driver)
        register.load_page()
        register.set_gender("male")
        register.set_first_name("muktar")
        register.set_last_name("mizi")
        register.set_email("mizimuktar0@gmail.com")  # Use already registered email
        register.set_password("123456", "123456")
        register.submit()

        register.driver.get_screenshot_as_file(".//screenshots//test_003_registration_existing_email.png")
        error = register.get_error()


        assert "The specified email already exists" in error
        print(" Registration failed Email is Already Registered")



def test_004_registration_invalid_email_format(driver):
        logger.info(f"Testing register page with invalid email format")
        register = Register_page(driver)
        register.load_page()
        register.set_gender("male")
        register.set_first_name("mizi")
        register.set_last_name("muktar")
        register.set_email("invalid-email@")  # wrong email format
        register.set_password("123456", "123456")
        register.submit()

        register.driver.get_screenshot_as_file(".//screenshots//test_004_registration_invalid_email_format.png")
        error = register.get_field_error()
        assert "Wrong email" in error
        print(" Registration failed Email is Invalid")
