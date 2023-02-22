from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html?username=Mickey&password=Mouse")
driver.maximize_window()

first_name_input = driver.find_element(By.ID, "fname");

if first_name_input.is_enabled():
    first_name_input.send_keys("Bartek")
    first_name_input.send_keys(Keys.ENTER)
else:
    print("Element nie jest dostępny")

time.sleep(5)