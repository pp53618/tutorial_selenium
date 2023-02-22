from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/")
driver.maximize_window()

driver.find_element(By.ID, "accept-choices").click()
tutorial_element = driver.find_element(By.ID, "navbtn_references")
webdriver.ActionChains(driver).move_to_element(tutorial_element).click(tutorial_element).perform()

time.sleep(5)