from datetime import date
import allure

from demoqa_tests.model.pages import practice_form_module
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby
from demoqa_tests.utils.parser_files import read_txt_file

practice_form = PracticePage()


@allure.label('owner', 'Aleksandr Popov')
@allure.feature('Tests DemoQA')
@allure.title('Successful registration')
def test_registration():
    student = Student(
        first_name='Alex',
        last_name='po',
        email='alexpo@email.com',
        phone='1111111111',
        address='NY',
        birthday=date(1991, 1, 1),
        gender='Male',
        subject='Maths',
        hobby=[Hobby.Music, Hobby.Sports],
        image='icons8-laptop-96 (1).png',
        state='NCR',
        city='Delhi'
    )
    with allure.step('Opening the registration page'):
        practice_form.open()
    with allure.step('Filling out the form'):
        practice_form.fill(student).submit()
    with allure.step('Checking the values of the resulting form'):
        practice_form.assert_results_registration(student)


@allure.label('owner', 'Aleksandr Popov')
@allure.feature('Tests DemoQA')
@allure.title('Successful registration with required fields')
def test_registration_required_field():
    with allure.step('Opening the registration page'):
        practice_form_module.opening()
    with allure.step('Filling out the form'):
        practice_form_module.fill_registration_form(*read_txt_file('student.txt'))
    with allure.step('Checking the values of the resulting form'):
        practice_form_module.assert_results_registration(
            [('Student Name', 'Aleksandr Popov'),
             ('Gender', 'Male'),
             ('Mobile', '8111111111')])
