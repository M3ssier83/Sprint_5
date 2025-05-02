from selenium.webdriver.common.by import By

class Locators:
    # главная страница
    STELLAR_BURGERS_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # логотип Stellar Burgers в шапке сайта
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор" в шапке сайта
    LOGIN_BUTTON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет" в шапке сайта

    # страница регистрации
    EMAIL_INPUT_REGISTRATION = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода email на странице регистрации
    NAME_INPUT_REGISTRATION = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')  # поле ввода имени на странице регистрации
    PASSWORD_INPUT_REGISTRATION = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля на странице регистрации
    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # кнопка отправки формы регистрации
    LOGIN_LINK_ON_REGISTRATION = (By.XPATH, '//a[text()="Войти"]')  # ссылка "Войти" на странице регистрации

    # страница логина
    EMAIL_INPUT_LOGIN = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода email на странице логина
    PASSWORD_INPUT_LOGIN = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля на странице логина
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # кнопка отправки формы логина
    REGISTER_LINK_ON_LOGIN = (By.XPATH, '//a[text()="Зарегистрироваться"]')  # ссылка "Зарегистрироваться" на странице логина
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')  # ссылка "Восстановить пароль" на странице логина # по факту не использовали в тестах, но может пригодиться позже

    # страница восстановления пароля
    LOGIN_LINK_ON_PASSWORD_RECOVERY = (By.XPATH, '//a[text()="Войти"]')  # ссылка "Войти" на странице восстановления пароля # по факту не использовали в тестах, но может пригодиться позже

    # личный кабинет
    PROFILE_SECTION = (By.XPATH, '//a[@href="/account/profile"]')  # раздел "Профиль" в личном кабинете # по факту не использовали в тестах, но может пригодиться позже
    ORDER_HISTORY_SECTION = (By.XPATH, '//a[@href="/account/order-history"]')  # раздел "История заказов" в личном кабинете # по факту не использовали в тестах, но может пригодиться позже
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # кнопка "Выход" в личном кабинете

    # конструктор
    ACTIVE_CONSTRUCTOR_TAB = (By.XPATH, '//div[contains(@class,"tab_tab_type_current__2BEPc")]')  # активная вкладка в конструкторе бургеров
    CONSTRUCTOR_TAB_BUNS = (By.XPATH, '//span[text()="Булки"]')  # вкладка "Булки" в конструкторе бургеров
    CONSTRUCTOR_TAB_FILLINGS = (By.XPATH, '//span[text()="Начинки"]')  # вкладка "Начинки" в конструкторе бургеров
    CONSTRUCTOR_TAB_SAUCES = (By.XPATH, '//span[text()="Соусы"]')  # вкладка "Соусы" в конструкторе бургеров

    # ошибки
    ERROR_MESSAGE_INPUT = (By.CSS_SELECTOR, '.input__error.text_type_main-default')  # сообщение об ошибке под полем ввода # по факту не использовали в тестах, но может пригодиться позже
    WRONG_PASSWORD_MESSAGE = (By.XPATH, '//p[contains(text(), "Некорректный пароль")]')  # сообщение об ошибке при неправильном пароле
