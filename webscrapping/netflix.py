import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from selenium.webdriver.support.ui import WebDriverWait



chrome = driver = webdriver.Chrome()
# netflix = driver.get("https://www.netflix.com/in/")
# max = driver.maximize_window()
# signin = driver.find_element(By.ID, "signIn").click()
# username = driver.find_element(By.ID, ":r0:").send_keys("madhumn772@gmail.com")
# password = driver.find_element(By.ID, ":r3:").send_keys("Navvi@25mnk")
# eye = driver.find_element(By.CSS_SELECTOR, ".default-ltr-cache-fmygl2.ea3diy34").click()
# signin_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
# lgnslp = time.sleep(20)

#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Function to automate Flipkart laptop navigation
def automate_flipkart_laptops():

    driver.implicitly_wait(10)

    driver.get("https://www.flipkart.com/pay-day-aug-bbdh-store")
    driver.maximize_window()


    driver.find_element(By.CLASS_NAME, "TSD49J").click()

    # Click on the "Gaming Laptops" section driver.find_element(By.XPATH, "//a[@title='Gaming Laptops']").click()


    time.sleep(5)


    driver.find_element(By.CSS_SELECTOR, ".fxf7w6.rgHxCQ").click()  # Adjust class names if necessary


    time.sleep(15)


    driver.quit()

automate_flipkart_laptops()



