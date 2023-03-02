from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.subjects.subject_api.subject_serializers.subjectSerializer import SubjectSerializer

class SubjectViewset(GenericModelViewSet):
    '''
    Generic Viewset for Subject
        - GET: list all subjects
        - POST: create a subject
        - GET(id): get a subject by id
        - PUT(id): update a subject by id
        - DELETE(id): delete a subject by id
    '''
    serializer_class = SubjectSerializer