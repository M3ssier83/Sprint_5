# Проверка, что по клику на кнопку «Конструктор» и на логотип Stellar Burgers можно перейти в конструктор (на главную страницу):

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import MAIN_PAGE_URL

def test_logo_redirects_to_constructor(driver, authorized_user):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Пользователь авторизуется и переходит в личный кабинет
    profile_button = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    profile_button.click()

    # Шаг 2: Кликаем по логотипу, чтобы вернуться в конструктор
    logo = driver.find_element(*Locators.STELLAR_BURGERS_LOGO)
    logo.click()
    # Явное ожидание: URL стал URL главной страницы
    wait.until(EC.url_to_be(MAIN_PAGE_URL))

    # Шаг 3: Проверка URL
    assert driver.current_url == MAIN_PAGE_URL, f"Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers не удался — URL отличается от ожидаемого. Ожидаемый: {MAIN_PAGE_URL}, текущий: {driver.current_url}"

def test_constructor_button_redirects_to_constructor(driver, authorized_user):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Пользователь авторизуется и переходит в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Шаг 2: Находим кнопку "Конструктор" и кликаем по ней
    constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON_HEADER)
    constructor_button.click()
    # Явное ожидание: URL стал URL главной страницы
    wait.until(EC.url_to_be(MAIN_PAGE_URL))

    # Шаг 3: Проверка URL
    assert driver.current_url == MAIN_PAGE_URL, f"Переход из личного кабинета в конструктор по кнопке «Конструктор» не удался — URL отличается от ожидаемого. Ожидаемый: {MAIN_PAGE_URL}, текущий: {driver.current_url}"

