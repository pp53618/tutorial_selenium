from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html")
driver.maximize_window()
#driver.find_element(By.ID, "clickOnMe").click()
#click_me_button = driver.find_element(By.ID, "clickOnMe")
#click_me_button.click()
#driver.find_element(By.TAG_NAME, "p").click()

# 1. obsługa alertu

#driver.find_element(By.ID, "clickOnMe").click()
#driver.switch_to.alert.accept()
#driver.find_element(By.ID, "clickOnMe").click()
#driver.switch_to.alert.dismiss()

# 2. wprowadzenie wartości do pola tekstowego

#driver.find_element(By.ID, "fname").send_keys("Bartek")

# 3. symulacja naciśniecia przycisku Enter

#driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

# 4. wybieranie opcji z selecta

#auto_select = Select(driver.find_element(By.TAG_NAME, "select"))
#auto_select.select_by_visible_text("Volvo")
#auto_select.select_by_value("saab")
#auto_select.select_by_index("2")

# 5. zaznaczanie checkboxa

#driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

# 6. zaznaczanie radio buttona

#driver.find_element(By.XPATH, "//input[@value='other']").click()

# 7. pobieranie tekstu z elementu

#print(driver.find_element(By.TAG_NAME, "h1").text)
#print(driver.find_element(By.ID, "clickOnMe").text)
#print(driver.find_element(By.TAG_NAME, "p").text)

# 8. pobranie tekstu z ukrytego elementu

#print(driver.find_element(By.TAG_NAME, "p").get_attribute("textContent"))
#driver.find_element(By.ID, "fname").send_keys("Bartek")
#print("Element text " + driver.find_element(By.ID, "fname").get_attribute("value"))

# 9. sprawdzanie, czy obrazek wyświetla się na stronie

#print(driver.find_element(By.ID, "smileImage").size.get("height"))
#print(driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight"))

# 10. przełączanie do nowego okna przeglądarki

driver.find_element(By.ID, "newPage").click()
print(driver.title)
current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

print(driver.title)
driver.switch_to.window(current_window_name)
print(driver.title)

time.sleep(5)