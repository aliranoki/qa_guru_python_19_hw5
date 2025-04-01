import os

from selene import browser, have, be, command

def test_form(setup_browser):
    browser.open('https://demoqa.com/automation-practice-form')

    # Заполнение формы
    browser.element('#firstName').should(be.visible).type('John')
    browser.element('#lastName').should(be.visible).type('Doe')
    browser.element('#userEmail').should(be.visible).type('john.doe@example.com')
    browser.element('[for="gender-radio-1"]').should(be.clickable).click()
    browser.element('#userNumber').should(be.visible).type('1234567890')
    browser.element('#dateOfBirthInput').perform(
        command.js.scroll_into_view).should(be.visible).click()

    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('2000')).click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('August')).click()
    browser.all('.react-datepicker__month div').element_by(have.exact_text('15')).click()

    browser.element('#subjectsInput').perform(
        command.js.scroll_into_view).should(be.visible).type('Arts').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()

    browser.element('#uploadPicture').should(be.clickable).type(os.getcwd() + "/picture.png")


    browser.element('#currentAddress').should(be.visible).type('123 Main Street, Apt 4B, New York, NY 10001')
    browser.element('#state').click().element('#react-select-3-input').set_value('Rajasthan').press_tab()
    browser.element('#city').click().element('#react-select-4-input').set_value('Jaiselmer').press_tab()

    # Отправка формы
    browser.element('#submit').perform(
        command.js.scroll_into_view).should(be.clickable).click()

    # Проверка результатов
    # Проверка заголовка модального окна
    browser.element('#example-modal-sizes-title-lg').should(
        have.exact_text('Thanks for submitting the form')
    )

    # Проверка данных в таблице
    browser.all('tbody tr')[0].should(
        have.exact_text('Student Name John Doe')
    )
    browser.all('tbody tr')[1].should(
        have.exact_text('Student Email john.doe@example.com')
    )
    browser.all('tbody tr')[2].should(
        have.exact_text('Gender Male')
    )
    browser.all('tbody tr')[3].should(
        have.exact_text('Mobile 1234567890')
    )
    browser.all('tbody tr')[4].should(
        have.exact_text('Date of Birth 15 August,2000')
    )
    browser.all('tbody tr')[5].should(
        have.exact_text('Subjects Arts')
    )
    browser.all('tbody tr')[6].should(
        have.exact_text('Hobbies Sports, Reading')
    )
    browser.all('tbody tr')[7].should(
        have.exact_text('Picture picture.png')
    )
    browser.all('tbody tr')[8].should(
        have.exact_text('Address 123 Main Street, Apt 4B, New York, NY 10001')
    )
    browser.all('tbody tr')[9].should(
        have.exact_text('State and City Rajasthan Jaiselmer')
    )