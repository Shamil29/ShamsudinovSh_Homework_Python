from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


def test_data_types():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(browser)
    calculator_page.field_waits()
    calculator_page.click_button_1()
    calculator_page.click_button_2()
    calculator_page.click_button_3()
    calculator_page.click_button_4()
    result = calculator_page.find_result()

    assert result == '15'

    browser.quit()
