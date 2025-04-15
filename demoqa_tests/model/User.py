import datetime
from enum import Enum


# Перечисление для пола
class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


# Перечисление для хобби
class Hobbies(Enum):
    SPORT = "Sports"
    MUSIC = "Music"
    READING = "Reading"


class User:
    first_name: str
    last_name: str
    user_email: str
    gender: Gender
    phone_number: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: Hobbies
    picture: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, user_email, gender, phone_number, date_of_birth, subjects, hobbies,
                 picture, address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.subjects = subjects
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
        self.state = state
        self.city = city
