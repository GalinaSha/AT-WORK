import time

import allure
from selenium.webdriver.common.by import By


class MyResumePageLocators:
    NEW_RESUME_BUTTON = (By.CLASS_NAME, "new-resume__link")
    ELLIPSIS_BUTTON = (By.CLASS_NAME, "card__dropdown")
    DELETE_ELLIPSIS_BUTTON = (By.CLASS_NAME, "dropdown-card__item--type--delete")
    DELETE_POPUP_BUTTON = (By.CLASS_NAME, "popup-bottom-template__btn--type--action-delete")
    ARCHIVE_ELLIPSIS_BUTTON = (By.CLASS_NAME, "dropdown-card__item--type--archive")





def open_create_form_resume_from_menu(selenium):
    with allure.step('Нажатие на кнопку "Новое резюме"'):
        selenium.find_element(*MyResumePageLocators.NEW_RESUME_BUTTON).click()


def delete_resume(selenium):
    with allure.step('Нажатие на кнопку "Многоточие"'):
        selenium.find_element(*MyResumePageLocators.ELLIPSIS_BUTTON).click()
    with allure.step('Нажатие на кнопку "Удалить"'):
        selenium.find_element(*MyResumePageLocators.DELETE_ELLIPSIS_BUTTON).click()
    with allure.step('Нажатие на кнопку "Удалить" в попапе подтверждения'):
        selenium.find_element(*MyResumePageLocators.DELETE_POPUP_BUTTON).click()


def archive_resume(selenium):
    with allure.step('Нажатие на кнопку "Многоточие"'):
        selenium.find_element(*MyResumePageLocators.ELLIPSIS_BUTTON).click()
    with allure.step('Нажатие на кнопку "Архивировать"'):
        selenium.find_element(*MyResumePageLocators.ARCHIVE_ELLIPSIS_BUTTON).click()