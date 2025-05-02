import pytest
from selenium import webdriver
from generator import Generator
from locators import Locators
from data import REGISTER_PAGE_URL, LOGIN_PAGE_URL, MAIN_PAGE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# фикстура для запуска браузера
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

# фикстура для генерации email
@pytest.fixture
def test_email():
    return Generator.generate_email()

# фикстура для генерации пароля
@pytest.fixture
def test_password():
    return Generator.generate_password()

# фикстура для регистрации пользователя
@pytest.fixture
def registered_user(driver, test_email, test_password):
    driver.get(REGISTER_PAGE_URL)

    # Заполнение формы регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NAME_INPUT_REGISTRATION)).send_keys("TestName")
    driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION).send_keys(test_email)
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION).send_keys(test_password)
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()

    # Подтверждение успешной регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON))

    return test_email, test_password

# фикстура для авторизации пользователя
@pytest.fixture
def authorized_user(driver, registered_user):
    email, password = registered_user
    driver.get(LOGIN_PAGE_URL)

    # Шаг 1: Заполняем поля логина
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT_LOGIN)).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(password)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Шаг 2: Дожидаемся редиректа после логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))

    # Возвращаем email, password — для совместимости
    return email, password