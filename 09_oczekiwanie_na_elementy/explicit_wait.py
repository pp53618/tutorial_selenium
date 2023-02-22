from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Waits2.html")
driver.maximize_window()

driver.find_element(By.ID, "clickOnMe").click()
wait.until(lambda wd: len(wd.find_element(By.TAG_NAME, "p")) == 1)
#wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'p')))
print(driver.find_element(By.TAG_NAME, "p").text)

