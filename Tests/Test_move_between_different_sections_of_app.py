from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_move_to_page_personal_account_by_button_personal_account_in_header(driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Нажимаем на кнопку "Личный кабинет" в шапке.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()
# Ожидаем загрузки страницы личного кабинета.
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9" and @href="/account/profile"]')))
# Проверяем url страницы личного кабинета.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

def test_move_to_page_constructor_from_page_account_by_button_constructor(driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Нажимаем на кнопку "Личный кабинет" в шапке.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()
# Ожидаем загрузки страницы личного кабинета.
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]')))
# Нажимаем кнопку Конструктор.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]').click()
# Ожидаем загрузки страницы конструктора, она же главная страница(ожидаем появления надписи "Соберите бургер").
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')))
# Проверяем адрес страницы конструктора/главной страницы.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_move_to_page_constructor_from_page_account_by_click_logo_stellar_burgers(driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Нажимаем на кнопку "Личный кабинет" в шапке.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()
# Ожидаем загрузки страницы личного кабинета.
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]')))
# Нажимаем на логотип приложения в шапке страницы.
    driver.find_element(By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]').click()
# Ожидаем загрузки страницы конструктора, она же главная страница(ожидаем появления надписи "Соберите бургер").
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')))
# Проверяем адрес страницы конструктора/главной страницы.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_loging_out_sucessfuly_by_clicking_button_exit_in_prtsonal_account_page(driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Нажимаем на кнопку "Личный кабинет" в шапке.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()
# Ожидаем загрузки страницы личного кабинета.
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]')))
# Нажимаем кнопку Выход.
    driver.find_element(By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]').click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Проверяем, что выход из аккаунта произошел и мы перешли на страницу ввода логина и пароля пользователя.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
