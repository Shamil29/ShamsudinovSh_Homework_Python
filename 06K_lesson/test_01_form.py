from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

first_name = 'Иван'
last_name = 'Петров'
address = 'Ленина, 55-3'
email = 'test@skypro.com'
zip_code = ""
phone = '+7985899998787'
city = 'Москва'
country = 'Россия'
job = "QA"
company = 'SkyPro'


def test_data_types():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    first_name_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=first-name]')
    first_name_input.clear()
    first_name_input.send_keys(first_name)

    last_name_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=last-name]')
    last_name_input.clear()
    last_name_input.send_keys(last_name)

    address_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=address]')
    address_input.clear()
    address_input.send_keys(address)

    email_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=e-mail]')
    email_input.clear()
    email_input.send_keys(email)

    zip_code_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=zip-code]')
    zip_code_input.clear()
    zip_code_input.send_keys(zip_code)

    phone_number_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=phone]')
    phone_number_input.clear()
    phone_number_input.send_keys(phone)

    city_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=city]')
    city_input.clear()
    city_input.send_keys(city)

    country_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=country]')
    country_input.clear()
    country_input.send_keys(country)

    job_position_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=job-position]')
    job_position_input.clear()
    job_position_input.send_keys(job)

    company_input = driver.find_element(
        By.CSS_SELECTOR, '.form-control[name=company]')
    company_input.clear()
    company_input.send_keys(company)

    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    driver.execute_script("arguments[0].click();", button)

    assert "danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "company").get_attribute("class")

    driver.quit()
