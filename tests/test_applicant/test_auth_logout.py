import allure

from pages.User.HeaderPage import logout
from pages.User.LoginPage import auth_email, auth_phone, should_be_profile


@allure.feature('Тест-сьют содержит проверки авторизации и выхода из аккаунта')
class TestAuthLogout:
    @allure.title('Авторизация по email')
    def test_auth_email(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)
        should_be_profile(selenium)

    @allure.title('Авторизация по номеру телефона')
    def test_auth_phone(self, go_to_url, selenium):
        auth_phone(go_to_url, selenium)
        should_be_profile(selenium)

    @allure.title('Выход из аккаунта')
    def test_logout(self, selenium, go_to_url):
        auth_email(go_to_url, selenium)
        logout(selenium)
