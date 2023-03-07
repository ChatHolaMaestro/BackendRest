# File which contains the SHORT serializers for each model
from rest_framework import serializers

# Student and Relative models
from apps.students.students_models import Student
from apps.students.students_models import Relative

# School Model
from apps.schools.school_models.schoolModels import School

# Teacher and Schedule models
from apps.teachers.teacher_models.teacherModels import Teacher, Schedule

# Request Model
from apps.requests.request_models.requestModels import Request

# Homework Model
from apps.homeworks.homework_models.homeworkModels import Homework

# --------------------------------------------SHORT SERIALIZERS--------------------------------------------

# Student and Relative serializers
class StudentSerializerShort(serializers.ModelSerializer):
    """
    Student Serializer SHORT:
        - id
        - name
        - last_name

    """

    class Meta:
        model = Student
        fields = ["id", "name", "last_name"]


class RelativeSerializerShort(serializers.ModelSerializer):
    """
    Relative Serializer SHORT:
        - id
        - name
        - last_name
    """

    class Meta:
        model = Relative
        fields = ["id", "name", "last_name"]


# School serializer
class SchoolSerializerShort(serializers.ModelSerializer):
    """
    School serializer SHORT:
        - id
        - name
    """

    class Meta:
        model = School
        fields = ("id", "name")


# Teacher and Schedule serializers
class TeacherSerializerShort(serializers.ModelSerializer):
    """
    Teacher serializer short
        - id
    """

    class Meta:
        model = Teacher
        # TODO add user field
        fields = ("id",)


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
