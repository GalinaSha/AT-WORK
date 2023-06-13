import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data_for_tests import ResumeData
from pages.Applicant.ApplicantPage import open_create_form_resume_from_new_resume
from pages.MainPage import go_applicant_page


class ResumeCreatePageLocators:
    AVATAR_BUTTON = (By.CLASS_NAME, "profile__avatar-btn")
    NEXT_BUTTON_1 = (By.CLASS_NAME, "steps__btn--type--next")

    POST_INPUT = (By.CLASS_NAME, "step-input--type--job-title")
    SALARY_INPUT = (By.CLASS_NAME, "step-input--type--job-salary")
    SALARY_CURRENCY_SELECTOR = (By.CLASS_NAME, "currency__select-input")
    SALARY_CURRENCY_USD = (By.CSS_SELECTOR, "[data-id='1780']")
    SALARY_CURRENCY_RUB = (By.CSS_SELECTOR, "[data-id='1779']")
    SPECIALISATION_BUTTON = (By.CLASS_NAME, "step-action-btn--specialization")
    PROFESSIONAL_AREA = (By.CSS_SELECTOR, "[data-id='8162']")
    SPECIALISATION_ITEM = (By.CSS_SELECTOR, "[data-id='8177']")
    SPECIALISATION_CHOOSE_BUTTON = (By.CLASS_NAME, "popup-rigth__btn-specializations-action")
    NEXT_BUTTON_2 = (By.CLASS_NAME, "steps__btn--type--next-step2")

    WORK_FORMAT_OFFICE = (By.CSS_SELECTOR, "[data-id='1776']")
    EMPLOYMENT_FULL = (By.CSS_SELECTOR, "[data-id='61']")
    SCHEDULE_FULL = (By.CSS_SELECTOR, "[data-id='94']")
    BUSINESS_TRIPS_READY = (By.CSS_SELECTOR, "[data-id='1446']")
    RELOCATION_CHECKBOX = (By.CLASS_NAME, "relocation__item-slider")
    RELOCATION_INPUT = (By.CSS_SELECTOR, "input.relocation__input")
    RELOCATION_SELECTOR = (By.CSS_SELECTOR, "[data-id='7906']")
    NEXT_BUTTON_3 = (By.CLASS_NAME, "steps__btn--type--next-step3")

    EXPERIENCE_CHECKBOX = (By.CLASS_NAME, "experience__item-switch")
    ADD_EXPERIENCE_BUTTON = (By.CLASS_NAME, "experience__add-btn")
    NAME_COMPANY_INPUT = (By.CLASS_NAME, "popup-experience__input--type--name-company")
    JOB_TITLE_INPUT = (By.CLASS_NAME, "popup-experience__input--type--job-title")
    WORK_PERIOD_MONTH_START_INPUT = (By.CLASS_NAME, "popup-experience__input--type--month-start")
    WORK_PERIOD_MONTH_START_SELECTOR = (By.CLASS_NAME, "dropdown-list__item--type--experience-month-start")
    WORK_PERIOD_YEAR_START_INPUT = (By.CLASS_NAME, "popup-experience__input--type--year-start")
    WORK_PERIOD_CHECKBOX = (By.CLASS_NAME, "popup-experience__item-switch")
    RESPONSIBILITIES_INPUT = (By.CLASS_NAME, "popup-experience__textarea--type--responsibilities")
    ACHIEVEMENTS_INPUT = (By.CLASS_NAME, "popup-experience__textarea--type--achievements")
    REASONS_FOR_LEAVING_INPUT = (By.CLASS_NAME, "popup-experience__textarea--type--reasons textarea-last")
    SAVE_EXPERIENCE_BUTTON = (By.CLASS_NAME, "popup-rigth__btn-experience-action")
    NEXT_BUTTON_4 = (By.CLASS_NAME, "steps__btn--type--next-step4")

    ADD_BASIC_EDUCATION_BUTTON = (By.CLASS_NAME, "step-action-btn--basic-education")
    NAME_INSTITUTE_INPUT = (By.CLASS_NAME, "popup-education__input--type--name-institute")
    SPECIALISATION_INPUT = (By.CLASS_NAME, "popup-education__input--type--specialization")
    DEPARTMENT_INPUT = (By.CLASS_NAME, "popup-education__input--type--faculty")
    YEAR_END_INPUT = (By.CLASS_NAME, "popup-education__input--type--year")
    SAVE_EDUCATION_BUTTON = (By.CLASS_NAME, "popup-rigth__btn-action--type--popup-education")

    ADD_ADDITIONAL_EDUCATION_BUTTON = (By.CLASS_NAME, "step-action-btn--basic-education")
    NAME_INSTITUTE_ADDITIONAL_INPUT = (By.CLASS_NAME, "additional-education__input--type--name-institution")
    NAME_HOST_ORGANIZATION_INPUT = (By.CLASS_NAME, "additional-education__input--type--organization")
    SPECIALISATION_ADDITIONAL_INPUT = (By.CLASS_NAME, "additional-education__input--type--specialization")
    YEAR_END_ADDITIONAL_INPUT = (By.CLASS_NAME, "additional-education__input additional-education__input--type--year")
    SAVE_ADDITIONAL_BUTTON = (By.CLASS_NAME, " popup-rigth__btn-action--type--additional-education")



def open_create_form_resume_from_applicant_page(selenium):
    with allure.step('Открытие формы создания резюме со страницы "Я соискатель"'):
        go_applicant_page(selenium)
        open_create_form_resume_from_new_resume(selenium)


def click_next(selenium, next_button_locator):
    with allure.step('Нажатие на кнопку "Далее"'):
        wait = WebDriverWait(selenium, 10)
        next_button = wait.until(EC.element_to_be_clickable(next_button_locator))
        next_button.click()


#нАДО ДОПИСАТЬ ПОТОМ ПОДУМАТЬ КАК ВСТАВИТЬ ФОТО
def change_avatar_resume(selenium):
    with allure.step('Нажатие на кнопку изменения аватара'):
        selenium.find_element(*ResumeCreatePageLocators.AVATAR_BUTTON).click()


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


def schedule_change(selenium):
    with allure.step('Нажатие на график работы "Полный день"'):
        selenium.find_element(*ResumeCreatePageLocators.SCHEDULE_FULL).click()


def business_trips_change(selenium):
    with allure.step('Нажатие на готовность к командировкам "Готова"'):
        selenium.find_element(*ResumeCreatePageLocators.BUSINESS_TRIPS_READY).click()


def relocation_change(selenium):
    with allure.step('Нажатие на чекбокс "Возможен переезд"'):
        selenium.find_element(*ResumeCreatePageLocators.RELOCATION_CHECKBOX).click()


def add_relocation_city(selenium):
    with allure.step('Ввод в поле "Город для возможного переезда"'):
        selenium.find_element(*ResumeCreatePageLocators.RELOCATION_INPUT).send_keys(ResumeData.city)
        selenium.find_element(*ResumeCreatePageLocators.RELOCATION_SELECTOR).click()


def experience_change(selenium):
    with allure.step('Нажатие на чекбокс "У меня есть опыт работы"'):
        selenium.find_element(*ResumeCreatePageLocators.EXPERIENCE_CHECKBOX).click()


def add_experience(selenium):
    with allure.step('Нажатие на кнопку "Добавить место работы"'):
        selenium.find_element(*ResumeCreatePageLocators.ADD_EXPERIENCE_BUTTON).click()
    with allure.step('Ввод в поле "Название компании"'):
        selenium.find_element(*ResumeCreatePageLocators.NAME_COMPANY_INPUT).send_keys(ResumeData.company_name)
    with allure.step('Ввод в поле "Должность"'):
        selenium.find_element(*ResumeCreatePageLocators.JOB_TITLE_INPUT).send_keys(ResumeData.job_title)
    with allure.step('Указание периода работа'):
        selenium.find_element(*ResumeCreatePageLocators.WORK_PERIOD_MONTH_START_INPUT).click()
        with allure.step('Выбор месяца начала работы'):
            selenium.find_element(*ResumeCreatePageLocators.WORK_PERIOD_MONTH_START_SELECTOR).click()
        with allure.step('Ввод года начала работы'):
            selenium.find_element(*ResumeCreatePageLocators.WORK_PERIOD_YEAR_START_INPUT).send_keys("2020")
        with allure.step('Нажатие на чекбокс "По настоящее время"'):
            selenium.find_element(*ResumeCreatePageLocators.WORK_PERIOD_CHECKBOX).click()
    with allure.step('Нажатие на кнопку "Сохранить"'):
        selenium.find_element(*ResumeCreatePageLocators.SAVE_EXPERIENCE_BUTTON).click()


def add_basic_education(selenium):
    with allure.step('Нажатие на кнопку "Добавить"'):
        selenium.find_element(*ResumeCreatePageLocators.ADD_EXPERIENCE_BUTTON).click()
    with allure.step('Ввод в поле "Название учебного заведения"'):
        selenium.find_element(*ResumeCreatePageLocators.NAME_INSTITUTE_INPUT).send_keys(ResumeData.institute_name)
    with allure.step('Ввод в поле "Специализация"'):
        selenium.find_element(*ResumeCreatePageLocators.SPECIALISATION_INPUT).send_keys(ResumeData.specialisation_edu)
    with allure.step('Ввод в поле "Факультет"'):
        selenium.find_element(*ResumeCreatePageLocators.DEPARTMENT_INPUT).send_keys(ResumeData.department_edu)
    with allure.step('Ввод в поле "Год окончания"'):
        selenium.find_element(*ResumeCreatePageLocators.YEAR_END_INPUT).send_keys("2017")
    with allure.step('Нажатие на кнопку "Сохранить"'):
        selenium.find_element(*ResumeCreatePageLocators.SAVE_EDUCATION_BUTTON).click()


def add_additional_education(selenium):
    with allure.step('Нажатие на кнопку "Добавить"'):
        selenium.find_element(*ResumeCreatePageLocators.ADD_EXPERIENCE_BUTTON).click()
    with allure.step('Ввод в поле "Учебное заведение"'):
        selenium.find_element(*ResumeCreatePageLocators.NAME_INSTITUTE_ADDITIONAL_INPUT).send_keys(ResumeData.institute_name)
    with allure.step('Ввод в поле "Проводившая организация"'):
        selenium.find_element(*ResumeCreatePageLocators.NAME_HOST_ORGANIZATION_INPUT).send_keys(ResumeData.host_organisation)
    with allure.step('Ввод в поле "Специализация"'):
        selenium.find_element(*ResumeCreatePageLocators.SPECIALISATION_ADDITIONAL_INPUT).send_keys(ResumeData.specialisation_edu)
    with allure.step('Ввод в поле "Год окончания"'):
        selenium.find_element(*ResumeCreatePageLocators.YEAR_END_ADDITIONAL_INPUT).send_keys("2018")
    with allure.step('Нажатие на кнопку "Сохранить"'):
        selenium.find_element(*ResumeCreatePageLocators.SAVE_ADDITIONAL_BUTTON).click()