import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://practicetestautomation.com/practice-test-login/')
    context.driver.maximize_window()

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

@when('I enter valid credentials')
def step_impl(context):
    try:

        username = context.driver.find_element(By.ID, 'username')  # Corrected method name
        username.send_keys('student')


        password = context.driver.find_element(By.ID, 'password')  # Corrected method name
        password.send_keys('Password123')


        submit = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit'))
        )
        submit.click()

    except Exception as e:
        print(f"Unexpected error: {e}")


@then('I should be redirected to the homepage')
def step_impl(context):

    WebDriverWait(context.driver, 10).until(
        EC.url_to_be('https://practicetestautomation.com/logged-in-successfully/')
    )

    assert context.driver.current_url == 'https://practicetestautomation.com/logged-in-successfully/', \
        f"Expected URL 'https://practicetestautomation.com/logged-in-successfully/', but got {context.driver.current_url}"

    time.sleep(5)
    context.driver.quit()