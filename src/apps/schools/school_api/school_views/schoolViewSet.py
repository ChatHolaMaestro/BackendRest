from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.schools.school_api.school_serializers.schoolSerializers import SchoolSerializer, SchoolManagerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class SchoolViewset(GenericModelViewSet):
    '''
    Generic Viewset for School
        - GET: list all schools
        - POST: create a school
        - GET(id): get a school by id
        - PUT(id): update a school by id
        - DELETE(id): delete a school by id
        - GET (name): search school by name
    '''
    serializer_class = SchoolSerializer
    
    @action(detail=False, methods=['get'])
    def search_name(self, request):
        '''
        Search school by name
        '''
        name = request.query_params.get('name')
        if name:
            queryset = self.get_queryset().filter(name__icontains=name)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'No school found'}, status=status.HTTP_400_BAD_REQUEST)

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