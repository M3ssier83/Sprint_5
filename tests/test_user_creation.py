# Проверка, что пользователь может успешно зарегистрироваться:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import VALID_NAME, LOGIN_PAGE_URL, REGISTER_PAGE_URL
from generator import Generator

def test_user_can_register_successfully(driver):
    wait = WebDriverWait(driver, 10)

    # Подготовка случайных валидных данных
    email = Generator.generate_email()
    password = Generator.generate_password()

    # Шаг 1: Переход на страницу регистрации
    driver.get(REGISTER_PAGE_URL)

    # Шаг 2: Заполняем поле имени (фиксированное валидное имя)
    name_input = driver.find_element(*Locators.NAME_INPUT_REGISTRATION)
    name_input.send_keys(VALID_NAME)

    # Шаг 3: Заполняем поле email (рандомный)
    email_input = driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION)
    email_input.send_keys(email)

    # Шаг 4: Заполняем поле пароля (рандомный валидный)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION)
    password_input.send_keys(password)

    # Шаг 5: Нажимаем кнопку "Зарегистрироваться"
    register_button = driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON)
    register_button.click()
    # Явное ожидание: произошел переход на страницу логина
    wait.until(EC.url_changes(driver.current_url))

    # Шаг 6: Проверяем, что текущий URL соответствует URL страницы логина
    current_url = driver.current_url
    assert current_url == LOGIN_PAGE_URL, f"После успешной регистрации не произошел переход на страницу логина — URL отличается от ожидаемого. Ожидаемый: {LOGIN_PAGE_URL}, текущий: {current_url}"


def test_user_registration_with_invalid_password(driver):
    wait = WebDriverWait(driver, 10)

    # Подготовка: валидный email и имя, но невалидный пароль
    email = Generator.generate_email()
    invalid_password = Generator.generate_invalid_password()

    # Шаг 1: Переход на страницу регистрации
    driver.get(REGISTER_PAGE_URL)

    # Шаг 2: Заполняем поле имени
    name_input = driver.find_element(*Locators.NAME_INPUT_REGISTRATION)
    name_input.send_keys(VALID_NAME)

    # Шаг 3: Заполняем поле email
    email_input = driver.find_element(*Locators.EMAIL_INPUT_REGISTRATION)
    email_input.send_keys(email)

    # Шаг 4: Вводим невалидный короткий пароль
    password_input = driver.find_element(*Locators.PASSWORD_INPUT_REGISTRATION)
    password_input.send_keys(invalid_password)

    # Шаг 5: Нажимаем кнопку "Зарегистрироваться"
    register_button = driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON)
    register_button.click()
    # Явное ожидание: появляется сообщение об ошибке
    error_message = wait.until(EC.visibility_of_element_located(Locators.WRONG_PASSWORD_MESSAGE))

    # Шаг 6: Проверка, что сообщение отображается
    assert error_message.is_displayed(), "Сообщение об ошибке при коротком пароле не отображается"

    # Шаг 7: Проверка текста ошибки
    expected_text = "Некорректный пароль"
    assert error_message.text == expected_text, f"Неверный текст ошибки. Ожидаемый: {expected_text}, текущий: {error_message.text}"
