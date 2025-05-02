# Проверка, что по клику на «Личный кабинет» можно перейти в личный кабинет:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import PROFILE_PAGE_URL

def test_navigation_to_personal_account(driver, authorized_user):
    wait = WebDriverWait(driver, 10)

    # Шаг 1, явное ожидание: появления кнопки "Личный кабинет" и клик на нее
    account_button = wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON))
    account_button.click()
    # Явное ожидание: переход в личный кабинет
    wait.until(EC.url_contains(PROFILE_PAGE_URL))

    # Шаг 3: Проверка текущего URL
    assert driver.current_url == PROFILE_PAGE_URL, f"Переход по кнопке «Личный кабинет» в личный кабинет не удался — URL отличается от ожидаемого. Ожидаемый: {PROFILE_PAGE_URL}, текущий: {driver.current_url}"
