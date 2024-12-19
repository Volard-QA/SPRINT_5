
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import HeaderLocators,LoginPageLocators, RegistrationPageLocators, MainPageLocators, ResetPasswordPage
from data import Credentials
from curl import *

class TestLoggingInAppFromDifferentPoints:

    def test_login_in_account_successful_by_button_enter_on_main_page(self, driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
        driver.find_element(*MainPageLocators.ENTER_ACCOUNT_BUTTON).click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
# Ожидаем прогрузки главной страницы приложения.
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
        assert driver.current_url == main_site

    def test_login_in_account_successful_by_button_personal_account_in_header(self, driver):
# Нажимаем кнопку "Личный кабинет" в шапке приложения.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
# Ожидаем прогрузки главной страницы приложения.
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
        assert driver.current_url == main_site

    def test_login_in_account_successful_by_button_enter_in_registration_form(self, driver):
# Нажимаем кнопку Личный кабинет в шапке приложения.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Нажимаем кнопку "Зарегистрироваться" в футере.
        driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
# Нажимаем кнопку "Войти" в форме регистрации
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.ENTER_ACCOUNT_BUTTON))
        driver.find_element(*RegistrationPageLocators.ENTER_ACCOUNT_BUTTON).click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
# Ожидаем прогрузки главной страницы приложения.
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
        assert driver.current_url == main_site

    def test_login_in_account_successful_by_button_enter_in_password_changing_form(self, driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
        driver.find_element(*MainPageLocators.ENTER_ACCOUNT_BUTTON).click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Нажимаем кнопку "Восстановить пароль".
        driver.find_element(*LoginPageLocators.RESET_PASSWORD_BUTTON).click()
# Ожидаем, что попадем на страницу восстановления пароля и станет видимой кнопка "Войти".
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ResetPasswordPage.ENTER_ACCOUNT_BUTTON))
# Нажимаем кнопку "Войти".
        driver.find_element(*ResetPasswordPage.ENTER_ACCOUNT_BUTTON).click()
# Ожидаем прогрузки страницы для ввода логина и пароля пользователя.
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
# Ожидаем прогрузки главной страницы приложения.
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
        assert driver.current_url == main_site