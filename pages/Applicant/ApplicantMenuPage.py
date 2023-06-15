import allure
from selenium.webdriver.common.by import By




class ApplicantMenuPageLocators:
    ROLE_SELECT = (By.CLASS_NAME, "select__header")
    ROLE_APPLICANT_ITEM = (By.CSS_SELECTOR, "[data-class='applicant']")
    MY_RESUME_PAGE = (By.CLASS_NAME, "summary ")



def change_role(selenium, role):
    with allure.step('Переключение роли в ЛК'):
        selenium.find_element(*ApplicantMenuPageLocators.ROLE_SELECT).click()
        selenium.find_element(*role).click()


def open_page_from_menu(selenium, page):
    with allure.step('Открытие вкладки в ЛК'):
        selenium.find_element(*page).click()