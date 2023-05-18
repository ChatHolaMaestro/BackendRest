from faker import Faker
fake = Faker()
import json

def createRandomUser():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = first_name + "." + last_name + "@gmail.com"
    email = email.lower()
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": fake.password(),
        "identification_type": "PA",
        "identification_number": fake.random_number(digits=10),
        "phone_number": fake.random_number(digits=10),
    }
    return user

createRandomUser()