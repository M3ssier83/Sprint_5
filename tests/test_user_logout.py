# Проверка, что из аккаунта можно выйти по кнопке «Выйти» в личном кабинете:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import LOGIN_PAGE_URL

def test_user_logout(driver, authorized_user):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Переход в личный кабинет
    wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    # Явное ожидание и шег 2: появление кнопки "Выход" и клик по ней
    logout_button = wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
    logout_button.click()
    # Явное ожидание: переход на страницу логина
    wait.until(EC.url_to_be(LOGIN_PAGE_URL))

    # Шаг 3: Проверка URL
    assert driver.current_url == LOGIN_PAGE_URL, f"После выхода из аккаунта не произошел переход на страницу логина — URL отличается от ожидаемого. Ожидаемый:{LOGIN_PAGE_URL}, текущий: {driver.current_url}"
