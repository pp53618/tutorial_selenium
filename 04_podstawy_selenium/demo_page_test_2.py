from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html")
driver.maximize_window()
driver.find_element(By.ID, "clickOnMe")
driver.find_element(By.NAME, "fname")
driver.find_element(By.LINK_TEXT, "Visit W3Schools.com!")
driver.find_element(By.PARTIAL_LINK_TEXT, "Visit W3Schools")
driver.find_element(By.CLASS_NAME, "topSecret")
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.TAG_NAME, "p")
driver.find_element(By.TAG_NAME, "label")
driver.find_element(By.CSS_SELECTOR, "a")
driver.find_element(By.CSS_SELECTOR, "img#smileImage")
driver.find_element(By.CSS_SELECTOR, "p.topSecret")
print(driver.find_element(By.CSS_SELECTOR, "th:first-child").text)
print(driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").text)
driver.find_element(By.XPATH, "/html/body/table/tbody/tr/th")
driver.find_element(By.XPATH, "//tbody//th")
driver.find_element(By.XPATH, "//th")
driver.find_element(By.XPATH, "//th[text()='Month']")
driver.find_element(By.XPATH, "//button[@id='clickOnMe']")
driver.find_element(By.XPATH, "//input[@id='fname']/following-sibling::table")

list_element = len(driver.find_elements(By.XPATH, "//th"))
print(list_element)


time.sleep(5)