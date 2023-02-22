from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/FileUpload.html")
driver.maximize_window()

upload_input = driver.find_element(By.ID, "myFile")
path = os.path.abspath("upload.txt")

driver.save_screenshot("screenshots/befor_upload.png")
upload_input.send_keys(path)
driver.save_screenshot("screenshots/after_upload.png")

time.sleep(5)