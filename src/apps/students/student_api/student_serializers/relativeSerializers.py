from rest_framework import serializers
from apps.students.student_models.student import Student
from apps.students.student_models.relative import Relative

class StudentSerializerForRelative(serializers.ModelSerializer):
    '''
    Student Serializer for Relative View:
        - id
        - name
        - last_name
        
    '''
    class Meta:
        model = Student
        fields = ['id', 'name', 'last_name']
    

class RelativeViewSerializer(serializers.ModelSerializer):
    '''
    Relative serializer:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - students (object)
    '''
    #students = StudentViewSerializer(many=True, read_only=True)
    students = StudentSerializerForRelative(many=True, read_only=True)
    class Meta:
        model = Relative
        exclude = ['is_active', 'created_date', 'modified_date', 'deleted_date']
        
class RelativeCreationSerializer(serializers.ModelSerializer):
    '''
    Relative Serializer for creation:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - students (numbers)
    '''
    class Meta:
        model = Relative
        exclude = ['is_active', 'created_date', 'modified_date', 'deleted_date']
