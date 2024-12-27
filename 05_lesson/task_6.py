from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FifefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FifefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys("tomsmith")
sleep(3)

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("SuperSecretPassword!")
sleep(3)

driver.find_element(By.CSS_SELECTOR, '.radius').click()

sleep(3)
driver.quit()
