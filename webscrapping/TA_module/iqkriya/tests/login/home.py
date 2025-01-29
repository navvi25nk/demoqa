import time
import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#from TA_module.iqkriya.locators.all_locators import *  # Imports everything from all_locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options  # Change 'chrome' to your browser (e.g., firefox, edge)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import Select




# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # You can use other browsers as well

# Navigate to demoqa and forms

# driver.get("https://demoqa.com")
# driver.maximize_window()
# time.sleep(6)
# forms = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/*[name()='svg'][1]")
# forms.click()
# time.sleep(10)




@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Optional: set an implicit wait
    yield driver  # Provide the WebDriver to the test
    driver.quit()  # Clean up the WebDriver after the test



@pytest.fixture(autouse=True)
def navigate_to_demoqa(driver):
    driver.get("https://demoqa.com")
    driver.maximize_window()
    time.sleep(6)


def test_navigate_demoqa(driver):
    # driver.get("https://demoqa.com")
    # driver.maximize_window()
    # time.sleep(6)
    forms = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/*[name()='svg'][1]")
    forms.click()
    time.sleep(5)
    page_content = driver.page_source
    assert "Forms" in page_content, "The page content does not contain 'Forms'."

def test_forms_elements(driver):
    test_navigate_demoqa(driver)
    dropdown=driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]")
    dropdown.click()
    time.sleep(4)
    try:
        checkbox_option = driver.find_element(By.ID, "item-1")
        checkbox_option.click()
        print("Checkbox option selected.")
    except Exception as e:
        print("Checkbox option not found or could not be clicked.")
        print("Error:", e)
    # checkbox_option=driver.find_element(By.ID,"item-1")
    # checkbox_option.click()
    time.sleep(4)

    if "Check Box" in driver.page_source:
        print("Page contains 'Check Boxes'. Test passed!")
    else:
        print("Page does not contain 'Check Boxes'. Test failed.")
    # selectcheck = Select(dropdown)
    # selectcheck.select_by_index(1)
    # assert "Check Boxes" in driver.page_source
    driver.find_element(By.XPATH,"//button[@title='Toggle']").click()
    time.sleep(4)
    checkbox = driver.find_element(By.XPATH, "//div[@class='body-height']")
    checkbox.click()

    selected_message = driver.page_source

    if "You have selected" in selected_message and (
            "desktop" in selected_message or "notes" in selected_message or "commands" in selected_message):
        print("Items found. Quitting the driver.")
        driver.quit()
    else:
        print("nk")
    # if not checkbox.is_selected():
    #     checkbox.click()
    #     print("Checkbox has been selected.")
    # else:
    #     print("Checkbox is already selected.")
    time.sleep(9)







