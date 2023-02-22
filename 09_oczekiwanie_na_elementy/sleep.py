from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Waits.html")
driver.maximize_window()

driver.find_element(By.ID, "clickOnMe").click()
time.sleep(5)
print(driver.find_element(By.TAG_NAME, "P").text)

