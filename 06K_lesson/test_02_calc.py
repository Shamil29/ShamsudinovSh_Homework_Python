from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


def test_slow_calculator():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    waits = driver.find_element(By.CSS_SELECTOR, '#delay')
    waits.clear()
    waits.send_keys('45')

    button_1 = driver.find_element(
        By.XPATH, '//span[text()="7"]')
    button_1.click()

    button_2 = driver.find_element(
        By.XPATH, '//span[text()="+"]')
    button_2.click()

    button_3 = driver.find_element(
        By.XPATH, '//span[text()="8"]')
    button_3.click()

    button_4 = driver.find_element(
        By.XPATH, '//span[text()="="]')
    button_4.click()

    waiter = WebDriverWait(driver, 50)
    waiter.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'screen'), '15')
                 )

    assert "15" in driver.find_element(By.CLASS_NAME, 'screen').text
    driver.quit()
