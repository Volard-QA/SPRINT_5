
import random
import string

generated_emails = set()
generated_passwords = set()

def generate_random_email(domain="yandex.ru"):
    while True:
        username_length = random.randint(10, 30)  # Длина имени пользователя от 10 до 50 символов
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        email = f"{username}@{domain}"
        # Проверяем уникальность
        if email not in generated_emails:
            generated_emails.add(email)  # Добавляем новый уникальный email в множество
            return email  # Возвращаем уникальный email

def generate_random_password(min_length=6, max_length=20):
    if min_length < 6:
        raise ValueError("Пароль должен быть не менее 6 символов.")

    while True:
        length = random.randint(min_length, max_length)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choices(characters, k=length))

        # Проверка уникальности
        if password not in generated_passwords:
            generated_passwords.add(password)  # Добавляем новый уникальный пароль в множество
            return password  # Возвращаем уникальный пароль
