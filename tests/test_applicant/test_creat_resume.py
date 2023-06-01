import allure
from selenium.webdriver.common.by import By

from src.actions.authorization import auth_email


@allure.feature('Проверки резюме')
@allure.story('Тест-сьют содержит проверки связанные с резюме')
class Test_Resume:
    @allure.title('Создание резюме')
    def test_auth_email(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)
        with allure.step('Проверка авторизации в нужный аккаунт'):
            selenium.find_element(By.CLASS_NAME, "authorization__button--enter").click()


