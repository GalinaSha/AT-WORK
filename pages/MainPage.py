import allure
from selenium.webdriver.common.by import By
from data_for_tests import ResumeData


class MainPageLocators:
    APPLICANT_PAGE_BUTTON = (By.CSS_SELECTOR, "div.choose-role__roles__block__employer-applicant>a[href='/applicant/']")





def go_applicant_page(selenium):
    with allure.step('Нажатие на роль "Я соискатель"'):
        selenium.find_element(*MainPageLocators.APPLICANT_PAGE_BUTTON).click()
