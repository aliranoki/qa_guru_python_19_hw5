from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_form(setup_browser, user):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered(user)







