import random
import string

# список популярных доменов для email
DOMAINS = ["yandex.ru", "gmail.com", "mail.ru", "outlook.com", "yahoo.com"]

class Generator:
    # генерация email со случайными буквами и случайным числом
    @staticmethod
    def generate_email():
        random_letters = ''.join(random.choices(string.ascii_lowercase, k=6))
        random_number = random.randint(100, 999)
        domain = random.choice(DOMAINS)
        email = f"{random_letters}{random_number}@{domain}"
        return email

    # генерация пароля длиной 6 символов (буквы и цифры)
    @staticmethod
    def generate_password():
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return password

    # генерация некорректного пароля: слишком короткий
    @staticmethod
    def generate_invalid_password():
        invalid_short_password = ''.join(random.choices(string.ascii_letters, k=4))
        return invalid_short_password