import allure
from selenium.webdriver.common.by import By
from data_for_tests import ResumeData


class ApplicantPageLocators:
    NEW_RESUME_BUTTON = (By.CSS_SELECTOR, "a.banners-list__item-link[href='/applicant/create/']")


def open_create_form_resume_from_new_resume(selenium):
    with allure.step('Нажатие на кнопку "Новое резюме"'):
        selenium.find_element(*ApplicantPageLocators.NEW_RESUME_BUTTON).click()