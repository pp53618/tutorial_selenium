from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html?username=Mickey&password=Mouse")
driver.maximize_window()

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox.click()

if checkbox.is_selected():
    print("Wartość jest zaznaczona! Odznaczam")
    checkbox.click()
else:
    print("Zaznaczam wartość")
    checkbox.click()

time.sleep(5)