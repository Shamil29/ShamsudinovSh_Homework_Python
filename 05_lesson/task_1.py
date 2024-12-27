from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    button_Add_Element = driver.find_element(
        By.CSS_SELECTOR, "[onclick='addElement()']").click()

button_Delete = driver.find_elements(
    By.CSS_SELECTOR, "[onclick='deleteElement()']")
print(f'Размер списка: {len(button_Delete)}')

sleep(5)
driver.quit()
