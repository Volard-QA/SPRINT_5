
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_login_in_account_successful_by_button_enter_on_main_page(driver):
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
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_login_in_account_successful_by_button_personal_account_in_header(driver):
# Нажимаем кнопку "Личный кабинет" в шапке приложения.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_login_in_account_successful_by_button_enter_in_registration_form(driver):
# Нажимаем кнопку Личный кабинет в шапке приложения.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_link__1fOlj")))
# Нажимаем кнопку "Зарегистрироваться" в футере.
    driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]').click()
# Нажимаем кнопку "Войти" в форме регистрации
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]')))
    driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

def test_login_in_account_successful_by_button_enter_in_password_changing_form(driver):
# Нажимаем кнопку "Войти в аккаунт" на главной странице приложения.
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
# Ожидаем, что попадаем на страницу ввода логина и пароля пользователя
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Нажимаем кнопку "Восстановить пароль".
    driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/forgot-password"]').click()
# Ожидаем, что попадем на страницу восстановления пароля и станет видимой кнопка "Войти".
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]')))
# Нажимаем кнопку "Войти".
    driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]').click()
# Ожидаем прогрузки страницы для ввода логина и пароля пользователя.
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')))
# Вводим валидные логин и пароль, нажимаем кнопку Войти.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
# Ожидаем прогрузки главной страницы приложения.
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
# Проверяем, что загрузилась именно главная страница приложения, т.е. вход в приложения произошел корректно.
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"