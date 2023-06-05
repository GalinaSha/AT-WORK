import logging
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from data_for_tests import LoginData
from pages.User.HeaderPage import profile_change_user, header_menu

class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.ID, "email-input")
    LOGIN_PASSWORD_INPUT = (By.ID, "auth-password")
    LOGIN_PHONE_TUB = (By.ID, "phone-authorization")
    LOGIN_PHONE_INPUT = (By.ID, "phone-input")
    LOGIN_BUTTON_CONTINUE = (By.CLASS_NAME, "authorization__button--continue")
    LOGIN_BUTTON_ENTER = (By.CLASS_NAME, "authorization__button--enter")


@allure.title('Авторизация в аккаунт по email c нажатием на "Enter"')
def auth_email(go_to_url, selenium):
    go_to_url(LoginData.login_url)

    with allure.step('Заполнение формы авторизации'):
        with allure.step('Ввод email'):
            selenium.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys(LoginData.email + Keys.ENTER)
        with allure.step('Ввод пароля'):
            selenium.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(LoginData.password + Keys.ENTER)

    logging.info('Waiting for login')


@allure.title('Авторизация в аккаунт по номеру телефона с нажатием на кнопки формы')
def auth_phone(go_to_url, selenium):
    go_to_url(LoginData.login_url)

    with allure.step('Заполнение формы авторизации'):
        with allure.step('Выбор входа по номеру телефона'):
            selenium.find_element(*LoginPageLocators.LOGIN_PHONE_TUB).click()
        with allure.step('Ввод номера телефона'):
            phone_input = selenium.find_element(*LoginPageLocators.LOGIN_PHONE_INPUT)
            phone_input.send_keys(Keys.HOME)  #из-за маски надо переместить курсор в начало
            phone_input.send_keys(LoginData.phone)
        with allure.step('Нажатие кнопки "Продолжить"'):
            selenium.find_element(*LoginPageLocators.LOGIN_BUTTON_CONTINUE).click()
        with allure.step('Ввод пароля'):
            selenium.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(LoginData.password)
        with allure.step('Нажатие кнопки "Войти"'):
            selenium.find_element(*LoginPageLocators.LOGIN_BUTTON_ENTER).click()

    logging.info('Waiting for login')


def should_be_profile(selenium):
    with allure.step('Проверка авторизации в нужный аккаунт'):
        with allure.step('Переключение на профиль физ.лица'):
            profile_change_user(selenium)
        with allure.step('Сравнение ID'):
            header_menu(selenium)
            profile_id_element = selenium.find_element(By.CLASS_NAME, "upper-case__profile-id")
            profile_id_text = profile_id_element.text
            assert profile_id_text == LoginData.user_ID, f"Ожидаемое значение: {LoginData.user_ID}, Фактическое значение: {profile_id_text}"
