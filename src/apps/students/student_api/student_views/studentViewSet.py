from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.students.student_api.student_serializers.studentSerializers import StudentViewSerializer, StudentCreationSerializer
from apps.students.student_api.student_serializers.relativeSerializers import RelativeViewSerializer, RelativeCreationSerializer

class StudentViewSet(GenericModelViewSet):
    '''
    Generic ViewSet for Student Model
        - GET: list all students
        - POST: create a student
        - GET(id): get a student by id
        - PUT(id): update a student by id
        - DELETE(id): delete a student by id
    '''
    serializer_class = StudentViewSerializer
    serializerCreation = StudentCreationSerializer
    serializerUpdate = StudentCreationSerializer

class RelativeViewSet(GenericModelViewSet):
    '''
    Generic ViewSet for Relative Model
        - GET: list all relatives
        - POST: create a relative
        - GET(id): get a relative by id
        - PUT(id): update a relative by id
        - DELETE(id): delete a relative by id
    '''
    serializer_class = RelativeViewSerializer
    serializerCreation = RelativeCreationSerializer
    serializerUpdate = RelativeCreationSerializer
    