import os
from selene import have, command, be
from selene.support.shared import browser
from datetime import datetime
from demoqa_tests.model.User import Gender, Hobbies


class RegistrationPage:
    # Локаторы
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = {
            Gender.MALE: browser.element('[for="gender-radio-1"]'),
            Gender.FEMALE: browser.element('[for="gender-radio-2"]')
        }
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.date_of_birth_year = browser.all('.react-datepicker__year-select option')
        self.date_of_birth_month = browser.all('.react-datepicker__month-select option')
        self.date_of_birth_day = browser.all('.react-datepicker__month div')

        self.subjects = browser.element('#subjectsInput')
        self.hobbies = {
            Hobbies.SPORT: browser.element('[for="hobbies-checkbox-1"]'),
            Hobbies.READING: browser.element('[for="hobbies-checkbox-2"]'),
            Hobbies.MUSIC: browser.element('[for="hobbies-checkbox-3"]'),
        }
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.state_input = browser.element('#react-select-3-input')
        self.city = browser.element('#city')
        self.city_input = browser.element('#react-select-4-input')
        self.submit_btn = browser.element('#submit')

    # Проверка регистрационных данных
        self.popup_title = browser.element('#example-modal-sizes-title-lg')
        self.student_name = browser.all('tbody tr')[0]
        self.student_email = browser.all('tbody tr')[1]
        self.student_gender = browser.all('tbody tr')[2]
        self.student_mobile = browser.all('tbody tr')[3]
        self.student_date_of_birth = browser.all('tbody tr')[4]
        self.student_subjects = browser.all('tbody tr')[5]
        self.student_hobbies = browser.all('tbody tr')[6]
        self.student_picture = browser.all('tbody tr')[7]
        self.student_address = browser.all('tbody tr')[8]
        self.student_state_and_city = browser.all('tbody tr')[9]


    # Заполнение формы
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.should(be.visible).type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.should(be.visible).type(value)
        return self

    def fill_user_email(self, value):
        self.user_email.should(be.visible).type(value)
        return self

    def set_gender(self, gender: Gender):
        self.gender[gender].perform(command.js.scroll_into_view).should(be.clickable).click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.should(be.visible).type(value)
        return self

    def fill_date_of_birth(self, date):
        self.date_of_birth.perform(command.js.scroll_into_view).should(be.visible).click()

        self.date_of_birth_year.element_by(have.exact_text(str(date.year))).click()

        month_name = date.strftime("%B")
        self.date_of_birth_month.element_by(have.exact_text(month_name)).click()

        self.date_of_birth_day.element_by(have.exact_text(str(date.day))).click()
        return self

    def choose_subjects(self, value):
        self.subjects.perform(command.js.scroll_into_view).should(be.visible).type(value).press_enter()
        return self

    def select_hobbies(self, *hobbies):
        for hobby_list in hobbies:  # hobby_list - это список хобби
            for hobby in hobby_list:  # Итерируем по каждому хобби в списке
                self.hobbies[hobby].perform(command.js.scroll_into_view).should(be.clickable).click()
        return self

    def upload_picture(self, value):
        self.picture.should(be.clickable).type(os.getcwd() + value)
        return self

    def fill_address(self, value):
        self.address.should(be.visible).type(value)
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view).click()
        self.state_input.set_value(name).press_enter()
        return self

    def fill_city(self, name):
        self.city.perform(command.js.scroll_into_view).click()
        self.city_input.set_value(name).press_tab()
        return self

    def submit_form(self):
        self.submit_btn.perform(command.js.click)
        return self

    # Проверка регистрационных данных
    def should_popup_title_be(self, value):
        self.popup_title.perform(command.js.scroll_into_view).should(have.exact_text(value))
        return self

    def should_student_name_be(self, value):
        self.student_name.should(have.exact_text(value))
        return self

    def should_student_email_be(self, value):
        self.student_email.should(have.exact_text(value))
        return self

    def should_student_gender_be(self, value):
        self.student_gender.should(have.exact_text(value))
        return self

    def should_student_mobile_be(self, value):
        self.student_mobile.should(have.exact_text(value))
        return self

    def should_student_date_of_birth_be(self, value):
        self.student_date_of_birth.should(have.exact_text(value))
        return self

    def should_student_subjects_be(self, value):
        self.student_subjects.should(have.exact_text(value))
        return self

    def should_student_hobbies_be(self, value):
        self.student_hobbies.should(have.exact_text(value))
        return self

    def should_student_picture_be(self, value):
        self.student_picture.should(have.exact_text(value))
        return self

    def should_student_address_be(self, value):
        self.student_address.should(have.exact_text(value))
        return self

    def should_student_state_and_city_be(self, value):
        self.student_state_and_city.should(have.exact_text(value))
        return self


    def register(self, user):
        # Заполнение формы
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_user_email(user.user_email)
        self.set_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.date_of_birth)
        self.choose_subjects(user.subjects)
        self.select_hobbies(user.hobbies)
        self.upload_picture('/'+user.picture)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_form()

    def should_have_registered(self, user):
        # Проверка результатов
        # Проверка заголовка модального окна
        self.should_popup_title_be('Thanks for submitting the form')
        # Проверка данных в таблице
        self.should_student_name_be(f'Student Name {user.first_name} {user.last_name}')
        self.should_student_email_be(f'Student Email {user.user_email}')
        self.should_student_gender_be(f'Gender {Gender.MALE.value}')
        self.should_student_mobile_be(f'Mobile {user.phone_number}')
        self.should_student_date_of_birth_be('Date of Birth ' + datetime
                                             .strptime(f'{user.date_of_birth}', "%Y-%m-%d")
                                             .strftime("%d %B,%Y"))
        self.should_student_subjects_be(f'Subjects {user.subjects}')
        self.should_student_hobbies_be(f'Hobbies {Hobbies.READING.value}, {Hobbies.SPORT.value}')
        self.should_student_picture_be(f'Picture {user.picture}')
        self.should_student_address_be(f'Address {user.address}')
        self.should_student_state_and_city_be(f'State and City {user.state} {user.city}')