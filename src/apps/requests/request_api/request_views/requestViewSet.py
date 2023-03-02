from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.requests.request_api.request_serializers.requestSerializer import RequestViewSerializer, RequestCreationSerializer

class RequestViewSet(GenericModelViewSet):
    '''
    Generic Request View Set
        - GET: list all requests
        - POST: create a request
        - GET(id): get a request by id
        - PUT(id): update a request by id
        - DELETE(id): delete a request by id
    '''
    serializer_class = RequestViewSerializer
    serializerCreation = RequestCreationSerializer
    serializerUpdate = RequestCreationSerializer
    