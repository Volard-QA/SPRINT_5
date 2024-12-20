# Перечень локаторов для автотестов приложения Stellar Burgers
from selenium.webdriver.common.by import By

class HeaderLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]') # Локатор кнопки "Учетная запись" в шапке приложения
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]') # Локатор кнопки "Конструктор" в шапке.
    APP_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]') #Локатор логотипа приложения в шапке.


class MainPageLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') # Локатор кнопки "Войти в аккаунт" на главной странице приложения
    CONSTRUCT_BURGER_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]') # Локатор надписи "Соберите бургер" на главной странице


class LoginPageLocators:
    REGISTER_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]')# Локатор кнопки "Зарегистрироваться" на странице ввода логина и пароля для входа пользователя.
    EMAIL_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]') # Локатор поля ввода email (логина) для входа пользователя на странице ввода логина и пароля.
    PASSWORD_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]') # Локатор поля ввода пароля для входа пользователя на странице ввода логина и пароля.
    LOGIN_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # Локатор кнопки "Войти" на странице ввода логина и пароля.
    RESET_PASSWORD_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/forgot-password"]') # Локатор кнопки "Восстановить пароль" на странице ввода логина и пароля.


class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]') # Локатор поля "Имя" на странице регистрации.
    EMAIL_FIELD = (By.XPATH, '(//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//label[text()="Email"]/following-sibling::input[@name="name"])') # Локатор поля "Email" на странице регистрации.
    PASSWORD_FIELD = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]') # Локатор поля "Пароль" на странице регистрации.
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') #Локатор кнопки "Зарегистрироваться" на странице регистрации.
    PASSWORD_ERROR_TEXT = (By.XPATH, '//p[@class="input__error text_type_main-default"]') # Локатор текста об ошибке ввода пароля.
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]') # Локатор кнопки "Войти" для возврата к странице ввода логина и пароля пользователя.

class ResetPasswordPage:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]') # Локатор кнопки "Войти" на странице сброса пароля.

class AccountPage:
    ACCOUNT_LINK_BUTTON = (By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9" and @href="/account/profile"]') # Локатор кнопки "Профиль" на странице учетной записи пользователя.
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]') # Локатор кнопки "Выход" на странице учетной записи пользователя.

class ConstructorSection:
    BULKI_SECTION_ACTIVE = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') # Локатор активной секции "Булки" в кнструкторе бургеров.
    HEAD_ACTIVE_SECTION = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[@class='text text_type_main-medium mb-6 mt-10']") # Локатор активной шапки раздела "Булки".
    HEAD_NONACTIVE_FIRST = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]') # Локатор первого неактивного раздела, например Соусы.
    HEAD_NONACTIVE_SECOND = (By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"][2]') # Локатор второго неактивного по счету раздела, например, Начинки.
    HEAD_SECTIONS_SAUCES_FILLINGS_ACTIVE = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default']") # Локатор активных шапок разделов конструктора.
