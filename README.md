# Sprint_5
# Составлены автотесты для приложения Stellar Burgers.
# В папке Tests по 4 файлам распределены тесты разных функциональностей приложения.
# В файле Test_Registration_System:
# 1) test_registration_with_valid_data - проверяет успешность регистрации пользователя с валидными данными имени, логина и пароля.
# 2) test_registration_with_invalid_password_error - проверяет появление ошибки о невалидном значении пароля.
# 
# В файле Test_Loging_In_App:
# 1) test_login_in_account_successful_by_button_enter_on_main_page - проверяет успешный вход в учетную запись по кнопке "Войти в аккаунт".
# 2) test_login_in_account_successful_by_button_personal_account_in_header - проверяет успешный вход в учетную запись по кнопке "Личный кабинет".
# 3) test_login_in_account_successful_by_button_enter_in_registration_form - проверяет успешный вход в учетную запись по кнопке "Войти" в форме регистрации.
# 4) test_login_in_account_successful_by_button_enter_in_password_changing_form - проверяет успешный вход в учетную запись по кнопке "Войти" в форме сброса пароля.
#
# В файле Test_Move_Between_Different_Sections_Of_App:
# 1) test_move_to_page_personal_account_by_button_personal_account_in_header - проверяет успешный переход зарегистрированного пользовател в личный кабинет по кнопке "Личный кабинет".
# 2) test_move_to_page_constructor_from_page_account_by_button_constructor - проверяет успешный зарегистрированного пользовател на главную страницу, к разделу конструктора бургеров, по кнопке "Конструктор".
# 3) test_move_to_page_constructor_from_page_account_by_click_logo_stellar_burgers - проверяет успешный зарегистрированного пользовател на главную страницу, к разделу конструктора бургеров, при клике на логотип приложения в шапке.
# 4) test_loging_out_sucessfuly_by_clicking_button_exit_in_prtsonal_account_page - проверяет успешный выход из аккаунта по кнопке "Выход" на странице аккаунта пользователя.
#
# В файле Test_change_sections_of_burgers_constructor:
# 1) test_section_bulki_in_constructor_on_main_page_app - проверяет, что на главной странице, в конструкторе, по умолчанию активным является раздел "Булки".
# 2) test_successful_switch_to_section_sauces_in_constructor - проверяет, что в конструкторе при клике на заголовок "Соусы" мы попадаем в раздел выбора соусов.
# 3) test_successful_switch_to_section_fillings_in_constructor - проверяет, что в конструкторе при клике на заголовок "Начинки" мы попадаем в раздел выбора начинок.
#
# Файл conftest.py содержит фикстуру активации драйвера, входа на главную страницу приложения и закрывания браузера по завершении теста.
# Файл helper содержит код генерации email и паролей для регистрации пользователя (требуется для теста регистрации пользователя в системе).
# Файл locators содержит классы локаторов для тестов и их описание.
# Файл curl.py содержит используемые url.
# Файл data.py содержит данные для тестов.
# Из-за ошибки merge при пуше коммита в депозитарий github пришлось произвести восстановление файлов проекта. 
#

