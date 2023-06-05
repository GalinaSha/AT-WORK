import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from data_for_tests import ResumeData


class ResumeCreatePageLocators:
    AVATAR_BUTTON = (By.CLASS_NAME, "profile__avatar-btn")
    NEXT_BUTTON = (By.CLASS_NAME, "steps__btn--type--next']")

    POST_INPUT = (By.CLASS_NAME, "step-input--type--job-title")
    SALARY_INPUT = (By.CLASS_NAME, "step-input--type--job-salary")
    SALARY_CURRENCY_SELECTOR = (By.CLASS_NAME, "currency__select-input")
    SALARY_CURRENCY_USD = (By.CSS_SELECTOR, "[data-id='1780']")
    SALARY_CURRENCY_RUB = (By.CSS_SELECTOR, "[data-id='1779']")
    SPECIALISATION_BUTTON = (By.CLASS_NAME, "step-action-btn--specialization")
    PROFESSIONAL_AREA = (By.XPATH, "//p[@class='list-area__text radio-item-text' and text()='Информационные технологии']")
    SPECIALISATION_ITEM = (By.XPATH, "//p[@class='specializations-list__item-text checkbox-item-text' and text()='Тестировщик']")
    SPECIALISATION_CHOOSE_BUTTON = (By.CLASS_NAME, "popup-rigth__btn-specializations-action")

    WORK_FORMAT_OFFICE = (By.CSS_SELECTOR, "[data-id='1776']")
    EMPLOYMENT_FULL = (By.CSS_SELECTOR, "[data-id='61']")
    SCHEDULE_FULL = (By.CSS_SELECTOR, "[data-id='94']")




#нАДО ДОПИСАТЬ ПОТОМ ПОДУМАТЬ КАК ВСТАВИТЬ ФОТО
def change_avatar_resume(selenium):
    with allure.step('Нажатие на кнопку изменения аватара'):
        selenium.find_element(*ResumeCreatePageLocators.AVATAR_BUTTON).click()


def click_next(selenium):
    with allure.step('Нажатие на кнопку "Далее"'):
        selenium.find_element(*ResumeCreatePageLocators.NEXT_BUTTON).click()


def post_change(selenium):
    with allure.step('Ввод в поле "Желаемая должность"'):
        selenium.find_element(*ResumeCreatePageLocators.POST_INPUT).send_keys(ResumeData.post)


def salary_change(selenium):
    with allure.step('Ввод в поле "Желаемая зарплата"'):
        selenium.find_element(*ResumeCreatePageLocators.SALARY_INPUT).send_keys(ResumeData.salary)
    with allure.step('Выбор валюты USD'):
        selenium.find_element(*ResumeCreatePageLocators.SALARY_CURRENCY_SELECTOR).click()
        selenium.find_element(*ResumeCreatePageLocators.SALARY_CURRENCY_USD).click()


def specialization_change(selenium):
    with allure.step('Нажатие на кнопку "Указать" в поле "Специализация"'):
        selenium.find_element(*ResumeCreatePageLocators.SPECIALISATION_BUTTON).click()
    with allure.step('Выбор профобласти "Информационные технологии"'):
        selenium.find_element(*ResumeCreatePageLocators.PROFESSIONAL_AREA).click()
    with allure.step('Выбор специализации "Тестировщик"'):
        selenium.find_element(*ResumeCreatePageLocators.SPECIALISATION_ITEM).click()
    with allure.step('Нажатие на кнопку "Выбрать"'):
        selenium.find_element(*ResumeCreatePageLocators.SPECIALISATION_CHOOSE_BUTTON).click()


def work_format_change(selenium):
    with allure.step('Нажатие на формат работы "Работа в офисе"'):
        selenium.find_element(*ResumeCreatePageLocators.WORK_FORMAT_OFFICE).click()


def employment_change(selenium):
    with allure.step('Нажатие на занятость "Полная занятость"'):
        selenium.find_element(*ResumeCreatePageLocators.EMPLOYMENT_FULL).click()

