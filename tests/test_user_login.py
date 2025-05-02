# Проверка, что пользователь может успешно войти по кнопке «Войти в аккаунт» на главной, через кнопку «Личный кабинет», через кнопку в форме регистрации и через кнопку в форме восстановления пароля:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generator import Generator
from data import VALID_NAME, MAIN_PAGE_URL, LOGIN_PAGE_URL, REGISTER_PAGE_URL
from locators import Locators

def test_login_from_main_page_button(driver):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Генерация уникальных email и пароля
    email = Generator.generate_email()
    password = Generator.generate_password()

    # Шаг 2: Регистрация нового пользователя
    driver.get(REGISTER_PAGE_URL)
    driver.find_element(*Locators.NAME_INPUT_REGISTRATION).send_keys(VALID_NAME)
    driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
    old_url = driver.current_url
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем смены URL после успешной регистрации
    wait.until(EC.url_changes(old_url))

    # Шаг 3: Переход на главную страницу
    driver.get(MAIN_PAGE_URL)

    # Шаг 4: Клик по кнопке «Войти в аккаунт»
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

    # Шаг 5: Ввод email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(password)

    # Шаг 6: Клик по кнопке входа
    old_url = driver.current_url
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на главную после успешного входа
    wait.until(EC.url_changes(old_url))

    # Шаг 7: Проверка URL
    current_url = driver.current_url
    assert current_url == MAIN_PAGE_URL, f"После успешной авторизации с главной страницы URL отличается от ожидаемого. Ожидаемый: {MAIN_PAGE_URL}, текущий: {current_url}"

def test_login_from_account_button(driver):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Генерация уникальных email и пароля
    email = Generator.generate_email()
    password = Generator.generate_password()

    # Шаг 2: Регистрация нового пользователя
    driver.get(REGISTER_PAGE_URL)
    driver.find_element(*Locators.NAME_INPUT_REGISTRATION).send_keys(VALID_NAME)
    driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
    old_url = driver.current_url
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на страницу логина
    wait.until(EC.url_changes(old_url))

    # Шаг 3: Переход на главную
    driver.get(MAIN_PAGE_URL)

    # Шаг 4: Клик по кнопке «Личный кабинет»
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Шаг 5: Ввод email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(password)

    # Шаг 6: Клик по кнопке входа
    old_url = driver.current_url
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на главную
    wait.until(EC.url_changes(old_url))

    # Шаг 7: Проверка URL
    current_url = driver.current_url
    assert current_url == MAIN_PAGE_URL, f"После успешной авторизации через кнопку «Личный кабинет» URL отличается от ожидаемого. Ожидаемый: {MAIN_PAGE_URL}, текущий: {current_url}"

def test_login_from_registration_form_link(driver):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Генерация уникальных email и пароля
    email = Generator.generate_email()
    password = Generator.generate_password()

    # Шаг 2: Регистрация нового пользователя
    driver.get(REGISTER_PAGE_URL)
    driver.find_element(*Locators.NAME_INPUT_REGISTRATION).send_keys(VALID_NAME)
    driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
    old_url = driver.current_url
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на страницу логина
    wait.until(EC.url_changes(old_url))

    # Шаг 3: Переход обратно на форму входа через ссылку
    driver.get(REGISTER_PAGE_URL)
    old_url = driver.current_url
    driver.find_element(*Locators.LOGIN_LINK_ON_REGISTRATION).click()
    # Явное ожидание: ожидаем перехода на страницу логина
    wait.until(EC.url_changes(old_url))

    # Шаг 4: Ввод email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(password)

    # Шаг 5: Клик по кнопке входа
    old_url = driver.current_url
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на главную
    wait.until(EC.url_changes(old_url))

    # Шаг 6: Проверка URL
    current_url = driver.current_url
    assert current_url == MAIN_PAGE_URL, f"После авторизации через форму регистрации URL отличается от ожидаемого. Ожидаемый: {MAIN_PAGE_URL}, текущий: {current_url}"

def test_login_from_password_recovery_link(driver):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Генерация уникальных email и пароля
    email = Generator.generate_email()
    password = Generator.generate_password()

    # Шаг 2: Регистрация нового пользователя
    driver.get(REGISTER_PAGE_URL)
    driver.find_element(*Locators.NAME_INPUT_REGISTRATION).send_keys(VALID_NAME)
    driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
    old_url = driver.current_url
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на страницу логина
    wait.until(EC.url_changes(old_url))

    # Шаг 3: Переход на страницу восстановления пароля
    driver.get(LOGIN_PAGE_URL)
    old_url = driver.current_url
    driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
    # Явное ожидание: ожидаем перехода на страницу восстановления
    wait.until(EC.url_changes(old_url))

    # Шаг 4: Переход обратно на логин
    old_url = driver.current_url
    driver.find_element(*Locators.LOGIN_LINK_ON_PASSWORD_RECOVERY).click()
    # Явное ожидание: ожидаем перехода обратно на логин
    wait.until(EC.url_changes(old_url))

    # Шаг 5: Ввод email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(password)

    # Шаг 6: Клик по кнопке входа
    old_url = driver.current_url
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Явное ожидание: ожидаем перехода на главную
    wait.until(EC.url_changes(old_url))

    # Шаг 7: Проверка URL
    current_url = driver.current_url
    assert current_url == MAIN_PAGE_URL, f"После авторизации через восстановление пароля URL отличается от ожидаемого. Ожидаемый: {MAIN_PAGE_URL}, текущий: {current_url}"
