from datetime import date
import pytest
from selene import browser
from demoqa_tests.model.User import User, Gender, Hobbies


@pytest.fixture(scope="session")
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()

@pytest.fixture
def user():
    return User(
        first_name="John",
        last_name="Doe",
        user_email="john.doe@example.com",
        gender=Gender.MALE,
        phone_number="1234567890",
        date_of_birth=date(year=2000, month=8, day=15),
        subjects="Arts",
        hobbies=[Hobbies.READING, Hobbies.SPORT],
        picture="picture.png",
        address="123 Main Street, Apt 4B, New York, NY 10001",
        state="Rajasthan",
        city="Jaiselmer"
    )