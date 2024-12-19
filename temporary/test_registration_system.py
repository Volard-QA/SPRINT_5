#Проверка успешной регистрации в приложении при вводе валидных значений логина и пароля.
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helper import generate_random_email, generate_random_password # Импортируем функции генерации email и пароля из helper.py
from locators import HeaderLocators,LoginPageLocators, RegistrationPageLocators
from data import Credentials
from curl import *

class TestRegistrationWithValidData:

    def test_successful_registration(self, driver):
#Нажимаем кнопку Личный кабинет в шапке приложения.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_BUTTON))

#Нажимаем кнопку "Зарегистрироваться" в футере.
        driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

# Генерируем случайные данные для регистрации
        random_email = generate_random_email()  # Генерация случайного email
        random_password = generate_random_password()  # Генерация случайного пароля

#Заполняем поля Имя, Email и Пароль валидными данными для регистрации в приложении, нажимаем кнопку.
        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(Credentials.name)
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(random_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url


class TestRegistrationWithInvalidPasswordError:

    def test_invalid_password_error(self, driver):
#Нажимаем кнопку Личный кабинет в шапке приложения.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_BUTTON))
#Нажимаем кнопку "Зарегистрироваться" в футере.
        driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
# Заполняем поле Пароль невалидным значением.
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(Credentials.incorrect_password)
#Снимаем фокус с активного поля Пароль.
        driver.execute_script("document.activeElement.blur();")
#Проверяем появление ошибки с текстом
        error_mes = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR_TEXT)
        )
        assert error_mes.text == 'Некорректный пароль'
