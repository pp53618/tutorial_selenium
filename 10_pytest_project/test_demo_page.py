import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("file:///C:/Users/paula/Desktop/Kurs%20Selenium%20Python%20od%20podstaw/Test.html")
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.quit()


def test_method(test_setup):
    assert driver.title == "Strona testowa"

def test_method2(test_setup):
    assert driver.title == "Strona testowa"
