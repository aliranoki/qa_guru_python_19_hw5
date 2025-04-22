from dataclasses import dataclass
import datetime
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Hobbies(Enum):
    SPORT = "Sports"
    MUSIC = "Music"
    READING = "Reading"


@dataclass
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
