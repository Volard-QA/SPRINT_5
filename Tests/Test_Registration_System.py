#Проверка успешной регистрации в приложении при вводе валидных значений логина и пароля.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_with_valid_data(driver):
#Нажимаем кнопку Личный кабинет в шапке приложения.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_link__1fOlj")))

#Нажимаем кнопку "Зарегистрироваться" в футере.
    driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]').click()

#Заполняем поля Имя, Email и Пароль валидными данными для регистрации в приложении, нажимаем кнопку .
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//input[@name="name"]').send_keys("Владислав")
    driver.find_element(By.XPATH, '(//div[@class="input pr-6 pl-6 input_type_text input_size_default"]//label[text()="Email"]/following-sibling::input[@name="name"])').send_keys("vladsemenov13314@yandex.ru")
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("Doctorwho1995")
    driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()

    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_registration_with_invalid_password_error(driver):

#Нажимаем кнопку Личный кабинет в шапке приложения.
    driver.find_element(By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/account"]').click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_link__1fOlj")))

#Нажимаем кнопку "Зарегистрироваться" в футере.
    driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]').click()

    # Заполняем поле Пароль невалидным значением.
    driver.find_element(By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//input[@name="Пароль"]').send_keys("qwer1")
#Снимаем фокус с активного поля Пароль.
    driver.execute_script("document.activeElement.blur();")

#Проверяем появление ошибки с текстом
    error_mes = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//p[@class="input__error text_type_main-default"]'))
    )
    assert error_mes.text == 'Некорректный пароль'

