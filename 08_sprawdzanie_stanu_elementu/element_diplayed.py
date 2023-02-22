from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html?username=Mickey&password=Mouse")
driver.maximize_window()

paragraph = driver.find_element(By.TAG_NAME, "p")

if paragraph.is_displayed():
    print("Is displayed")
    print(paragraph.text)
else:
    print("Is not displayed")
    print(paragraph.get_attribute("textContent"))


time.sleep(5)