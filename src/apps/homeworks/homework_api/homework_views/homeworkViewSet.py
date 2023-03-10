from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.homeworks.homework_api.homework_serializers.homeworkSerializer import HomeworkViewSerializer, HomeworkCreationSerializer

class HomeworkViewSet(GenericModelViewSet):
    '''
    ViewSet for Homework model
        - GET: list all homeworks
        - POST: create a homework
        - GET(id): get a homework by id
        - PUT(id): update a homework by id
        - DELETE(id): delete a homework by id
    '''
    serializer_class = HomeworkViewSerializer
    serializerCreation = HomeworkCreationSerializer
    serializerUpdate = HomeworkCreationSerializer
    