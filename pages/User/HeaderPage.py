import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class HeaderPageLocators:
    PROFILE_HEADER = (By.CLASS_NAME, "upper-case__profile-user")
    PROFILE_CHANGE_USER = (By.CLASS_NAME, "upper-case__profile-return")
    LOGOUT_BUTTON = (By.ID, "profile-logout")


def header_menu(selenium):
    with allure.step('Наведение на выпадающее меню в хедере'):
        profile_hover = selenium.find_element(*HeaderPageLocators.PROFILE_HEADER)
        action_chains = webdriver.ActionChains(selenium)
        action_chains.move_to_element(profile_hover).perform()


def profile_change_user(selenium):
    header_menu(selenium)
    with allure.step('Переключение аккаунта на физлицо'):
        profile_user_change = selenium.find_element(*HeaderPageLocators.PROFILE_CHANGE_USER)
        selenium.execute_script("arguments[0].click();", profile_user_change)


def logout(selenium):
    header_menu(selenium)
    with allure.step('Нажатие кнопки "Выйти"'):
        selenium.find_element(*HeaderPageLocators.LOGOUT_BUTTON).click()
