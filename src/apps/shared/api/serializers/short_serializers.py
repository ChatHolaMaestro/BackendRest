# File which contains the SHORT serializers for each model
from rest_framework import serializers

# User and Person Model
from apps.users.models.user import User, Person

# Student and Relative models
from apps.students.models import Student, Relative

# School and SchoolManager Model
from apps.schools.models import School, SchoolManager

# Teacher and Schedule models
from apps.teachers.models import Teacher, Schedule

# Request Model
from apps.requests.request_models.requestModels import Request

# Homework Model
from apps.homeworks.homework_models.homeworkModels import Homework


# --------------------------------------------SHORT SERIALIZERS--------------------------------------------


# User and Person serializers
class UserSerializerShort(serializers.ModelSerializer):
    """
    User serializer SHORT
        - id
        - first_name
        - last_name
        - email
        - phone_number
        - identification_type
        - identification_number
    """

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "identification_type",
            "identification_number",
        )


class PersonSerializerShort(serializers.ModelSerializer):
    """
    Person serializer SHORT
        - id
        - first_name
        - last_name
        - email
        - phone_number
        - identification_type
        - identification_number
    """

    class Meta:
        model = Person
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "identification_type",
            "identification_number",
        )


# Student and Relative serializers
class StudentSerializerShort(serializers.ModelSerializer):
    """
    Student Serializer SHORT:
        - id
        - first_name
        - last_name

    """

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name"]


class RelativeSerializerShort(serializers.ModelSerializer):
    """
    Relative Serializer SHORT:
        - id
        - first_name
        - last_name
    """

    class Meta:
        model = Relative
        fields = ["id", "first_name", "last_name"]


# School and School Manager serializer
class SchoolSerializerShort(serializers.ModelSerializer):
    """
    School serializer SHORT:
        - id
        - name
    """

    class Meta:
        model = School
        fields = ("id", "name")


class SchoolManagerSerializerShort(serializers.ModelSerializer):
    """
    School Manager serializer SHORT
        - id
        - user (object)
    """

    class Meta:
        model = SchoolManager
        fields = ("id", "user")


# Teacher and Schedule serializers
class TeacherSerializerShort(serializers.ModelSerializer):
    """
    Teacher serializer short
        - id
        - user (object)
    """

    user = UserSerializerShort()

    class Meta:
        model = Teacher
        fields = ("id", "user")


class ScheduleSerializerShort(serializers.ModelSerializer):
    """
    Schedule serializer short
        - id
        - day
        - start_hour
        - end_hour
        - request_type
    """

    class Meta:
        model = Schedule
        fields = ("id", "day", "start_hour", "end_hour", "request_type")


# Request serializer
class RequestSerializerShort(serializers.ModelSerializer):
    """
    Request serializer short
        - id
        - status
        - request_type
        - contact_times
    """

    class Meta:
        model = Request
        fields = ("id", "status", "request_type", "contact_times")


# Homework serializer
class HomeworkSerializerShort(serializers.ModelSerializer):
    """
    Homework serializer short
        - id
        - status
        - topic
        - details
        - time_spent
        - scheduled_date
    """

    class Meta:
        model = Homework
        fields = ("id", "status", "topic", "details", "time_spent", "scheduled_date")
