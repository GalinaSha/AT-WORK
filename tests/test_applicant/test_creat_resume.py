import allure

from pages.Applicant.ResumeCreatePage import *

from pages.User.LoginPage import auth_email


@allure.feature('Проверки резюме')
@allure.story('Тест-сьют содержит проверки связанные с резюме')
class TestResumeCreate:
    @allure.title('Создание резюме только обязательные поля')
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





