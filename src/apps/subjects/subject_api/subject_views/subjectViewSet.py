from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.subjects.subject_api.subject_serializers.subjectSerializer import SubjectSerializer

class SubjectViewset(GenericModelViewSet):
    '''
    Generic Viewset for Subject
    '''
    serializer_class = SubjectSerializer