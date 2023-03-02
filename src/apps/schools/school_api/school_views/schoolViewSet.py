from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.schools.school_api.school_serializers.schoolSerializers import SchoolSerializer, SchoolManagerSerializer

class SchoolViewset(GenericModelViewSet):
    '''
    Generic Viewset for School
        - GET: list all schools
        - POST: create a school
        - GET(id): get a school by id
        - PUT(id): update a school by id
        - DELETE(id): delete a school by id
    '''
    serializer_class = SchoolSerializer

class SchoolManagerViewset(GenericModelViewSet):
    '''
    Generic Viewset for School Manager
        - GET: list all school managers
        - POST: create a school manager
        - GET(id): get a school manager by id
        - PUT(id): update a school manager by id
        - DELETE(id): delete a school manager by id
    '''
    serializer_class = SchoolManagerSerializer