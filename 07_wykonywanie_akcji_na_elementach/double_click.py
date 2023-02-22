from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/DoubleClick.html")
driver.maximize_window()

button = driver.find_element(By.ID, "bottom")
#webdriver.ActionChains(driver).double_click(button).perform()
webdriver.ActionChains(driver).context_click(button).perform()

time.sleep(5)