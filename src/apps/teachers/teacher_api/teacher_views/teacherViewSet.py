from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.teachers.teacher_api.teacher_serializers.teacherSerializers import TeacherViewSerializer, TeacherCreationSerializer
from apps.teachers.teacher_api.teacher_serializers.scheduleSerializer import ScheduleViewSerializer, ScheduleCreationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TeacherViewSet(GenericModelViewSet):
    '''
    Generic viewset for teacher model
        - GET: list all teachers
        - POST: create a teacher
        - GET(id): get a teacher by id
        - PUT(id): update a teacher by id
        - DELETE(id): delete a teacher by id
        - GET (subject): search teacher by subject
    '''
    serializer_class = TeacherViewSerializer
    serializerCreation = TeacherCreationSerializer
    serializerUpdate = TeacherCreationSerializer
    
    @action(detail=False, methods=['get'])
    def search_subject(self, request):
        '''
        Search teacher by subject
        '''
        subject = request.query_params.get('subject')
        if subject:
            queryset = self.get_queryset().filter(subjects__name__icontains=subject)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'No teacher found'}, status=status.HTTP_400_BAD_REQUEST)
    

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
