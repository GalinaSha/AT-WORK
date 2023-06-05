import allure

from pages.Applicant.ResumeCreatePage import click_next, post_change, salary_change, specialization_change, \
    work_format_change
from pages.User.LoginPage import auth_email
from data_for_tests import ResumeData


@allure.feature('Проверки резюме')
@allure.story('Тест-сьют содержит проверки связанные с резюме')
class TestResumeCreate:
    @allure.title('Создание резюме только обязательные поля')
    def test_create_resume(self, go_to_url, selenium):
        auth_email(go_to_url, selenium)
        go_to_url(ResumeData.resume_create_url)

        with allure.step('Заполнение формы создания резюме'):
            click_next(selenium)
            post_change(selenium)
            salary_change(selenium)
            specialization_change(selenium)
            click_next(selenium)
            work_format_change(selenium)





