from rest_framework import serializers
from apps.students.student_models.studentModels import Student, Relative

class RelativeSerializerForStudent(serializers.ModelSerializer):
    '''
    Relative Serializer for Student View:
        - id
        - name
        - last_name 
    '''
    class Meta:
        model = Relative
        fields = ['id', 'name', 'last_name']


class StudentViewSerializer(serializers.ModelSerializer):
    '''
    Student Serializer for view:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - grade
        - sex
        - age
        - working_hours
        - relatives (object)
    '''
    relatives = RelativeSerializerForStudent(many=True, read_only=True)
    class Meta:
        model = Student
        exclude = ['is_active', 'created_date', 'modified_date', 'deleted_date']

class StudentCreationSerializer(serializers.ModelSerializer):
    '''
    Student Serializer for creation:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - grade
        - sex
        - age
        - working_hours
        - relatives (numbers) 
    '''
    class Meta:
        model = Student
        exclude = ['is_active', 'created_date', 'modified_date', 'deleted_date']
        