from rest_framework import serializers
from apps.requests.request_models.requestModels import Request
from apps.shared.shared_api.shared_serializers.ShortSerializers import StudentSerializerShort, TeacherSerializerShort, HomeworkSerializerShort
from apps.subjects.subject_api.subject_serializers.subjectSerializer import SubjectSerializer

class RequestViewSerializer(serializers.ModelSerializer):
    '''
    Request Serializer for View
        - id
        - status
        - request_type
        - created_date
        - contact_times
        - student (object)
        - teacher (object)
        - subject (object)
    '''
    student = StudentSerializerShort()
    teacher = TeacherSerializerShort()
    subject = SubjectSerializer()
    homework = HomeworkSerializerShort() #could be null
            
    class Meta:
        model = Request
        fields = ['id', 'status', 'request_type','created_date', 'contact_times', 'student', 'teacher', 'subject', 'homework']

class RequestCreationSerializer(serializers.ModelSerializer):
    '''
    Request Serializer for Creation
        - status
        - request_type
        - contact_times
        - student (id)
        - teacher (id)
        - subject (id)
    '''
    class Meta:
        model = Request
        fields = ['status', 'request_type', 'contact_times', 'student', 'teacher', 'subject']