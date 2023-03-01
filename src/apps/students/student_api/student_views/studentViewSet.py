from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.students.student_api.student_serializers.studentSerializers import StudentViewSerializer, StudentCreationSerializer
from apps.students.student_api.student_serializers.relativeSerializers import RelativeViewSerializer, RelativeCreationSerializer

class StudentViewSet(GenericModelViewSet):
    '''
    Generic ViewSet for Student Model
    '''
    serializer_class = StudentViewSerializer
    serializerCreation = StudentCreationSerializer
    serializerUpdate = StudentCreationSerializer

class RelativeViewSet(GenericModelViewSet):
    '''
    Generic ViewSet for Relative Model
    '''
    serializer_class = RelativeViewSerializer
    serializerCreation = RelativeCreationSerializer
    serializerUpdate = RelativeCreationSerializer
    