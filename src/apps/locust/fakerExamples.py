from faker import Faker
import random

fake = Faker()
RequestType = ["TAREAS", "REFUERZO", "CUALQUIERA"] 
WeekDays = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]

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


def createRandomSchool():
    school_name = fake.company() + " School"
    school = {
        "name": school_name,
        "address": fake.address(),
        "has_morning_hours": True,
        "has_afternoon_hours": False
    }
    return school

def createRandomSchoolManager():
    user = random.randint(1, 10)
    school = random.randint(1, 8)
    
    school_manager = {
        "user": user,
        "school": school,
    }
    return school_manager

def createRandomStudent():
    school = random.randint(1, 4)
    age = random.randint(5, 18)
    relative = random.randint(1, 10)
    
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "identification_type": "TI",
        "identification_number": fake.random_number(digits=10),
        "phone_number": fake.random_number(digits=10),
        "grade": "1",
        "sex": "M",
        "age": age,
        "working_hours": "M",
        "school": school,
        "relatives": [relative],
    }
    return student


def createRandomRelative():
    relative = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "identification_type": "CC",
        "identification_number": fake.random_number(digits=10),
        "phone_number": fake.random_number(digits=10),
    }
    return relative


def createRandomSchedule():

    day_of_week = fake.random_element(elements=WeekDays)
    request = fake.random_element(elements=RequestType)
    teacher = random.randint(1, 5)

    schedule = {
        "day_of_week": day_of_week,
        "start_time": "14:30:00",
        "end_time": "16:30:00",
        "request_type": request,
        "teacher": teacher,
    }
    return schedule


def createRandomRequest():
    student = random.randint(1, 16)
    teacher = random.randint(1, 5)
    subject = random.randint(1, 8)
    
    request = {
        "status": "COMPLETADO",
        "request_type": "CUALQUIERA",
        "contact_times": 3,
        "student": student,
        "teacher": teacher,
        "subject": subject,
    }
    return request
