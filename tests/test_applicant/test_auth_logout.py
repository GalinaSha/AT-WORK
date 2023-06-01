import allure
from selenium.webdriver.common.by import By

from pages.User.header import header_menu, profile_change_user, logout
from src.actions.authorization import auth_email, auth_phone


@allure.feature('Тест-сьют содержит проверки авторизации и выхода из аккаунта')
class Test_Auth_Logout:

    @allure.title('Авторизация по mail')
    def test_auth_email(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)

        with allure.step('Проверка авторизации в нужный аккаунт'):
            with allure.step('Переключение на профиль физ.лица'):
                profile_change_user(selenium)

            with allure.step('Сравнение ID'):
                header_menu(selenium)
                profile_id_element = selenium.find_element(By.CLASS_NAME, "upper-case__profile-id")
                profile_id_text = profile_id_element.text

                expected_id = "ID: 35095"
                assert profile_id_text == expected_id, f"Ожидаемое значение: {expected_id}, Фактическое значение: {profile_id_text}"


    @allure.title('Выход из аккаунта')
    def test_logout(self, selenium):
        logout(selenium)


    @allure.title('Авторизация по номеру телефона')
    def test_auth_phone(self, go_to_url, selenium):
        auth_phone(go_to_url, selenium)

        with allure.step('Проверка авторизации в нужный аккаунт'):
            with allure.step('Переключение на профиль физ.лица'):
                profile_change_user(selenium)

            with allure.step('Сравнение ID'):
                header_menu(selenium)
                profile_id_element = selenium.find_element(By.CLASS_NAME, "upper-case__profile-id")
                profile_id_text = profile_id_element.text

                expected_id = "ID: 35095"
                assert profile_id_text == expected_id, f"Ожидаемое значение: {expected_id}, Фактическое значение: {profile_id_text}"
