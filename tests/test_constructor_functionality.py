# Проверка, что в разделе "Конструктор" работают переходы к разделам:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import MAIN_PAGE_URL

def test_constructor_tabs_functionality(driver):
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Переход на главную страницу
    driver.get(MAIN_PAGE_URL)

    # Шаг 2: Кликаем по вкладке "Соусы"
    driver.find_element(*Locators.CONSTRUCTOR_TAB_SAUCES).click()
    # Явное ожидание: вкладка "Соусы" стала активной
    wait.until(EC.text_to_be_present_in_element(Locators.ACTIVE_CONSTRUCTOR_TAB, "Соусы"))
    active_tab = driver.find_element(*Locators.ACTIVE_CONSTRUCTOR_TAB).text
    assert active_tab == "Соусы", "Вкладка 'Соусы' не стала активной после клика"

    # Шаг 3: Кликаем по вкладке "Начинки"
    driver.find_element(*Locators.CONSTRUCTOR_TAB_FILLINGS).click()
    # Явное ожидание: вкладка "Начинки" стала активной
    wait.until(EC.text_to_be_present_in_element(Locators.ACTIVE_CONSTRUCTOR_TAB, "Начинки"))
    active_tab = driver.find_element(*Locators.ACTIVE_CONSTRUCTOR_TAB).text
    assert active_tab == "Начинки", "Вкладка 'Начинки' не стала активной после клика"

    # Шаг 4: Кликаем по вкладке "Булки"
    driver.find_element(*Locators.CONSTRUCTOR_TAB_BUNS).click()
    # Явное ожидание: вкладка "Булки" стала активной
    wait.until(EC.text_to_be_present_in_element(Locators.ACTIVE_CONSTRUCTOR_TAB, "Булки"))
    active_tab = driver.find_element(*Locators.ACTIVE_CONSTRUCTOR_TAB).text
    assert active_tab == "Булки", "Вкладка 'Булки' не стала активной после клика"

