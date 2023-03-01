from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.teachers.teacher_api.teacher_serializers.teacherSerializers import TeacherViewSerializer, TeacherCreationSerializer
from apps.teachers.teacher_api.teacher_serializers.scheduleSerializer import ScheduleViewSerializer, ScheduleCreationSerializer

class TeacherViewSet(GenericModelViewSet):
    '''
    Generic viewset for teacher model
    '''
    serializer_class = TeacherViewSerializer
    serializerCreation = TeacherCreationSerializer
    serializerUpdate = TeacherCreationSerializer

class ScheduleViewSet(GenericModelViewSet):
    '''
    Generic viewset for schedule model
    '''
    serializer_class = ScheduleViewSerializer
    serializerCreation = ScheduleCreationSerializer
    serializerUpdate = ScheduleCreationSerializer
