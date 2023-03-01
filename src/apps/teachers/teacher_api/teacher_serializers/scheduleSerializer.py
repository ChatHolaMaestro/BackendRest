from rest_framework import serializers
from apps.teachers.teacher_models.teacherModels import Schedule
from apps.teachers.teacher_api.teacher_serializers.teacherSerializers import TeacherSerializerShort

class ScheduleViewSerializer(serializers.ModelSerializer):
    '''
    Schedule serializer for view
        - id
        - day
        - start_hour
        - end_hour
        - request_type
        - teacher (object)
    '''
    teacher = TeacherSerializerShort(read_only=True)
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'start_hour', 'end_hour', 'request_type', 'teacher')

class ScheduleCreationSerializer(serializers.ModelSerializer):
    '''
    Schedule serializer for creation
        - day
        - start_hour
        - end_hour
        - request_type
        - teacher (id)
    '''
    class Meta:
        model = Schedule
        fields = ('day', 'start_hour', 'end_hour', 'request_type', 'teacher')

class ScheduleSerializerShort(serializers.ModelSerializer):
    '''
    Schedule serializer short
        - id
        - day
        - start_hour
        - end_hour
        - request_type
    '''
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'start_hour', 'end_hour', 'request_type')