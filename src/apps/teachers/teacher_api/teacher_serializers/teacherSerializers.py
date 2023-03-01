from rest_framework import serializers
from apps.teachers.teacher_models.teacherModels import Teacher
from apps.subjects.subject_api.subject_serializers.subjectSerializer import SubjectSerializer
from apps.shared.shared_api.shared_serializers.ShortSerializers import ScheduleSerializerShort

class TeacherViewSerializer(serializers.ModelSerializer):
    '''
    Teacher serializer for view
        - id
        - subjects (objects)
        - schedules (objects)
    '''
    subjects = SubjectSerializer(many=True, read_only=True)
    schedules = ScheduleSerializerShort(many=True, read_only=True)
    class Meta:
        model = Teacher
        #TODO add user field
        fields = ('id', 'subjects', 'schedules')

class TeacherCreationSerializer(serializers.ModelSerializer):
    '''
    Teacher serializer for creation
        - subjects (ids)
    '''
    class Meta:
        model = Teacher
        #TODO add user field
        fields = ('subjects',)

