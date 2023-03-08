from rest_framework import serializers
from apps.schools.school_models.schoolModels import School, SchoolManager
from apps.shared.shared_api.shared_serializers.ShortSerializers import SchoolSerializerShort

class SchoolSerializer(serializers.ModelSerializer):
    '''
    School serializer for view
        - id
        - name
        - address
        - has_morning_hours
        - has_afternoon_hours
    '''
    class Meta:
        model = School
        fields = ('id', 'name', 'address', 'has_morning_hours', 'has_afternoon_hours')

class SchoolManagerViewSerializer(serializers.ModelSerializer):
    '''
    School Manager serializer
        - id
        - school (object)
        - user (object)
    '''
    school = SchoolSerializerShort()
    #TODO: Add user field
    class Meta:
        model = SchoolManager
        fields = ['id','school']

class SchoolManagerCreationSerializer(serializers.ModelSerializer):
    '''
    School Manager serializer
        - id
        - school (id)
        - user (id) 
    '''
    
    class Meta:
        model = SchoolManager
        fields = ['id','school',]