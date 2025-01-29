import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # You can use other browsers as well

# Navigate to Twitter
driver.get("https://demoqa.com")