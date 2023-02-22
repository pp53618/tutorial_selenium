from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html?username=Mickey&password=Mouse")
driver.maximize_window()

elements = driver.find_elements(By.TAG_NAME, "p")

if len(elements) > 0:
    print("Element istnieje")
else:
    print("Element nie istnieje")

try:
    driver.find_elements(By.TAG_NAME, "p")
    print("Element istnieje")
except NoSuchElementException:
    print("Brak Elementu")


time.sleep(2)