from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

#CRUD WITH GENERAL VIEWSET
class GenericModelViewSet(viewsets.ModelViewSet):
    serializer_class = None
    serializerCreation = None
    serializerUpdate = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)
    
    def list(self, request, *args, **kwargs):
        '''
        List all objects of the model
        
        
        params
            -none
        '''
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        '''
        Create an object of the model
        
        
        params
            -Fields of the model
        '''
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        '''
        Get an object of the model by id
        
        
        params
            -id (int): id of the object
        '''
        instance = self.get_object()
        if instance:
            return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        '''
        Update an object of the model by id
        
        
        params
            -Fields of the model
        '''
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, *args, **kwargs):
        '''
        Delete an object of the model (logical delete)
        
        
        params
            -id (int): id of the object
        '''
        instance = self.get_object()
        if instance:
            instance.is_active = False
            instance.save()
            return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    #Override this method to use a different serializer to create or update an object
    def get_serializer(self, *args, **kwargs):
        #Creation serializer
        if self.action == 'create':
            if self.serializerCreation:
                return self.serializerCreation(*args, **kwargs)
        #Update, retrieve, patch serializer
        elif self.action == 'update':
            if self.serializerUpdate:
                return self.serializerUpdate(*args, **kwargs)
        
        return super().get_serializer(*args, **kwargs)
        