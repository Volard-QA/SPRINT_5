# Перечень локаторов для автотестов приложения Stellar Burgers
from selenium.webdriver.common.by import By

class HeaderLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]') # Локатор кнопки "Учетная запись" в шапке приложения
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]')
    APP_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]')


class MainPageLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') # Локатор кнопки "Войти в аккаунт" на главной странице приложения
    CONSTRUCT_BURGER_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')


class LoginPageLocators:
    REGISTER_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]')
    EMAIL_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/forgot-password"]')


class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]')
    EMAIL_FIELD = (By.XPATH, '(//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//label[text()="Email"]/following-sibling::input[@name="name"])')
    PASSWORD_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    PASSWORD_ERROR_TEXT = (By.XPATH, '//p[@class="input__error text_type_main-default"]')
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]')

class ResetPasswordPage:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]')

class AccountPage:
    ACCOUNT_LINK_BUTTON = (By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9" and @href="/account/profile"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')

class ConstructorSection:
    BULKI_SECTION_ACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')
    HEAD_ACTIVE_SECTION = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[@class='text text_type_main-medium mb-6 mt-10']")
    HEAD_NONACTIVE_SAUCES = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]')
    HEAD_NONACTIVE_FILLINGS = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"][2]')
    HEAD_SECTIONS_SAUCES_FILLINGS_ACTIVE = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default']")
