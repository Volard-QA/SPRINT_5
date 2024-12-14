import pytest
from selenium import webdriver
@pytest.fixture (scope='function')
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()  # Закрытие драйвера после завершения теста