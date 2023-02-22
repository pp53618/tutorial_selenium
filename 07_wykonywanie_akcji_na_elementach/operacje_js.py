from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html")
driver.maximize_window()
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "newPage"))

wartosc = "Bartek"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element(By.ID, "fname"))

time.sleep(5)