import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from TA_module.iqkriya.locators.all_locators import *  # Imports everything from all_locators
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



# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # You can use other browsers as well

forms = driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) div:nth-child(1) div:nth-child(2) svg")