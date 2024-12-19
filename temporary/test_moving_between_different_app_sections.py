
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import HeaderLocators,LoginPageLocators, AccountPage, MainPageLocators
from data import Credentials
from curl import *

class TestMovingToPersonalAccountPage:

    def test_move_to_personal_account_with_button_personal_account_in_header(self, driver):
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
# Нажимаем на кнопку "Личный кабинет" в шапке.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
# Ожидаем загрузки страницы личного кабинета.
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountPage.ACCOUNT_LINK_BUTTON))
# Проверяем url страницы личного кабинета.
        assert driver.current_url == account_url

class TestMovingToSectionBurgerConstructor:

    def test_move_to_page_constructor_from_page_account_by_button_constructor(self, driver):
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
# Нажимаем на кнопку "Личный кабинет" в шапке.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
# Ожидаем загрузки страницы личного кабинета.
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountPage.ACCOUNT_LINK_BUTTON))
# Нажимаем кнопку Конструктор.
        driver.find_element(*HeaderLocators.CONSTRUCTOR_BUTTON).click()
# Ожидаем загрузки страницы конструктора, она же главная страница(ожидаем появления надписи "Соберите бургер").
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCT_BURGER_TEXT))
# Проверяем адрес страницы конструктора/главной страницы.
        assert driver.current_url == main_site

    def test_move_to_page_constructor_from_page_account_by_click_logo_stellar_burgers(self, driver):
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
# Нажимаем на кнопку "Личный кабинет" в шапке.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
# Ожидаем загрузки страницы личного кабинета.
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountPage.ACCOUNT_LINK_BUTTON))
# Нажимаем на логотип приложения в шапке страницы.
        driver.find_element(*HeaderLocators.APP_LOGO).click()
# Ожидаем загрузки страницы конструктора, она же главная страница(ожидаем появления надписи "Соберите бургер").
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCT_BURGER_TEXT))
# Проверяем адрес страницы конструктора/главной страницы.
        assert driver.current_url == main_site

class TestLoggingOutFromAccount:
    def test_loging_out_sucessfuly_by_clicking_button_exit_in_prtsonal_account_page(self, driver):
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
# Нажимаем на кнопку "Личный кабинет" в шапке.
        driver.find_element(*HeaderLocators.ACCOUNT_BUTTON).click()
# Ожидаем загрузки страницы личного кабинета.
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AccountPage.ACCOUNT_LINK_BUTTON))
# Нажимаем кнопку Выход.
        driver.find_element(*AccountPage.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
# Проверяем, что выход из аккаунта произошел и мы перешли на страницу ввода логина и пароля пользователя.
        assert driver.current_url == login_url
