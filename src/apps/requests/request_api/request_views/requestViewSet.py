from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.requests.request_api.request_serializers.requestSerializer import RequestViewSerializer, RequestCreationSerializer

class RequestViewSet(GenericModelViewSet):
    '''
    Generic Request View Set
    '''
    serializer_class = RequestViewSerializer
    serializerCreation = RequestCreationSerializer
    serializerUpdate = RequestCreationSerializer
    