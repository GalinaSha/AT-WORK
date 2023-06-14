import time

import allure

from pages.Applicant.ResumeCreatePage import *

from pages.User.LoginPage import auth_email


@allure.feature('Проверки резюме')
@allure.story('Тест-сьют содержит проверки связанные с резюме')
class TestResumeCreate:
    @allure.title('Создание резюме с заполнением всех полей')
    def test_create_resume(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)
        open_create_form_resume_from_applicant_page(selenium)

        with allure.step('Заполнение формы создания резюме'):
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_1)
            post_change(selenium)
            salary_change(selenium)
            specialization_change(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_2)
            work_format_change(selenium)
            employment_change(selenium)
            schedule_change(selenium)
            business_trips_change(selenium)
            relocation_change(selenium)
            add_relocation_city(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_3)
            experience_change(selenium)
            add_experience(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_4)
            add_basic_education(selenium)
            add_additional_education(selenium)
            add_language(selenium)
            add_key_skills(selenium)
            driver_license_category_change(selenium)
            have_a_car_change(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_5)
            about_me(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_6)
            add_portfolio(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_7)
            add_video_resume(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_8)
            click_agreement_checkbox(selenium)
            click_next(selenium, ResumeCreatePageLocators.PUBLICATION_FREE_BUTTON)

    @allure.title('Создание резюме с заполнением всех полей')
    def test_delete_resume(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)


    @allure.title('Создание резюме с заполнением только обязательных полей')
    def test_create_resume(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)
        open_create_form_resume_from_applicant_page(selenium)

        with allure.step('Заполнение формы создания резюме'):
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_1)
            post_change(selenium)
            specialization_change(selenium)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_2)
            time.sleep(10)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_3)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_4)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_5)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_6)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_7)
            click_next(selenium, ResumeCreatePageLocators.NEXT_BUTTON_8)
            click_agreement_checkbox(selenium)
            click_next(selenium, ResumeCreatePageLocators.PUBLICATION_FREE_BUTTON)
