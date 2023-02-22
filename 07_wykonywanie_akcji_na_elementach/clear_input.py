from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html")
driver.maximize_window()

usermane_input = driver.find_element(By.NAME, "username")
usermane_input.clear()
usermane_input.send_keys("PonuryAdam")


time.sleep(5)