from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_section_bulki_in_constructor_on_main_page_app(driver):
    #Проверяем, что при первоначальной загрузке главной страницы приложения с конструктором выбран раздел "Булки".
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')))

    section_bulki = driver.find_element(By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//h2[@class='text text_type_main-medium mb-6 mt-10']")

    assert section_bulki.text == 'Булки'

def test_successful_switch_to_section_sauces_in_constructor(driver):
# Проверяем успешное переключение на раздел конструктора "Соусы".
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')))

    driver.find_element(By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]').click()

    section_sauces = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default']")

    assert section_sauces.text == 'Соусы'

def test_successful_switch_to_section_fillings_in_constructor(driver):
# Проверяем успешное переключение на раздел конструктора "Начинки".
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')))

    driver.find_element(By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"][2]').click()

    section_fillings = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[@class='text text_type_main-default']")

    assert section_fillings.text == 'Начинки'
