from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FifefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(
    service=FifefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
search_input.send_keys("1000")
sleep(3)

search_clear = driver.find_element(By.CSS_SELECTOR, '[type="number"]').clear()
search_input.send_keys("999")
sleep(3)

driver.quit()
