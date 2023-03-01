from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.schools.school_api.school_serializers.schoolSerializers import SchoolSerializer, SchoolManagerSerializer

class SchoolViewset(GenericModelViewSet):
    '''
    Generic Viewset for School
    '''
    serializer_class = SchoolSerializer

class SchoolManagerViewset(GenericModelViewSet):
    '''
    Generic Viewset for School Manager
    '''
    serializer_class = SchoolManagerSerializer