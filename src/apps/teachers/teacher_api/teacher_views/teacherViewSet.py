from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.teachers.teacher_api.teacher_serializers.teacherSerializers import TeacherViewSerializer, TeacherCreationSerializer
from apps.teachers.teacher_api.teacher_serializers.scheduleSerializer import ScheduleViewSerializer, ScheduleCreationSerializer

class TeacherViewSet(GenericModelViewSet):
    '''
    Generic viewset for teacher model
        - GET: list all teachers
        - POST: create a teacher
        - GET(id): get a teacher by id
        - PUT(id): update a teacher by id
        - DELETE(id): delete a teacher by id
    '''
    serializer_class = TeacherViewSerializer
    serializerCreation = TeacherCreationSerializer
    serializerUpdate = TeacherCreationSerializer

class ScheduleViewSet(GenericModelViewSet):
    '''
    Generic viewset for schedule model
        - GET: list all schedules
        - POST: create a schedule
        - GET(id): get a schedule by id
        - PUT(id): update a schedule by id
        - DELETE(id): delete a schedule by id
    '''
    serializer_class = ScheduleViewSerializer
    serializerCreation = ScheduleCreationSerializer
    serializerUpdate = ScheduleCreationSerializer
