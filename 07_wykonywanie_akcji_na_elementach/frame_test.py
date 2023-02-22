from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/iFrameTest.html")
driver.maximize_window()

print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)

time.sleep(5)