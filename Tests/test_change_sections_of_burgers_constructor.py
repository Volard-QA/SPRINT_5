
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorSection

class TestSectionBurgerConstructor:

    def test_section_bulki_in_constructor_on_main_page_app(self, driver):
    #Проверяем, что при первоначальной загрузке главной страницы приложения с конструктором выбран раздел "Булки".
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ConstructorSection.BULKI_SECTION_ACTIVE))

        section_bulki = driver.find_element(*ConstructorSection.HEAD_ACTIVE_SECTION)

        assert section_bulki.text == 'Булки'

    def test_successful_switch_to_section_sauces_in_constructor(self, driver):
# Проверяем успешное переключение на раздел конструктора "Соусы".
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ConstructorSection.BULKI_SECTION_ACTIVE))

        driver.find_element(*ConstructorSection.HEAD_NONACTIVE_FIRST).click()

        section_sauces = driver.find_element(*ConstructorSection.HEAD_SECTIONS_SAUCES_FILLINGS_ACTIVE)

        assert section_sauces.text == 'Соусы'

    def test_successful_switch_to_section_fillings_in_constructor(self, driver):
# Проверяем успешное переключение на раздел конструктора "Начинки".
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ConstructorSection.BULKI_SECTION_ACTIVE))

        driver.find_element(*ConstructorSection.HEAD_NONACTIVE_SECOND).click()

        section_fillings = driver.find_element(*ConstructorSection.HEAD_SECTIONS_SAUCES_FILLINGS_ACTIVE)

        assert section_fillings.text == 'Начинки'
