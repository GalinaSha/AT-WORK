import logging
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@allure.title('Авторизация в аккаунт по email c нажатием на "Enter"')
def auth_email(go_to_url, selenium):
    go_to_url("https://atwrk.ru/auth/?login=yes&backurl=/")

    with allure.step('Заполнение формы авторизации'):
        with allure.step('Ввод email'):
            selenium.find_element(By.ID, "email-input").send_keys("tester-wolf@mail.ru" + Keys.ENTER)
        with allure.step('Ввод пароля'):
            selenium.find_element(By.ID, "auth-password").send_keys("33Test!!" + Keys.ENTER)

    logging.info('Waiting for login')


@allure.title('Авторизация в аккаунт по номеру телефона с нажатием на кнопки формы')
def auth_phone(go_to_url, selenium):
    go_to_url("https://atwrk.ru/auth/?login=yes&backurl=/")

    with allure.step('Заполнение формы авторизации'):
        with allure.step('Выбор входа по номеру телефона'):
            selenium.find_element(By.ID, "phone-authorization").click()
        with allure.step('Ввод номера телефона'):
            phone_input = selenium.find_element(By.ID, "phone-input")
            phone_input.send_keys(Keys.HOME)  #из-за маски надо переместить курсор в начало
            phone_input.send_keys("9818544643")
        with allure.step('Нажатие кнопки "Продолжить"'):
            selenium.find_element(By.CLASS_NAME, "authorization__button--continue").click()
        with allure.step('Ввод пароля'):
            selenium.find_element(By.ID, "auth-password").send_keys("33Test!!")
        with allure.step('Нажатие кнопки "Войти"'):
            selenium.find_element(By.CLASS_NAME, "authorization__button--enter").click()

    logging.info('Waiting for login')



