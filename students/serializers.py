from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'name', 'dob', 'registration_date']
        read_only_fields = ['id', 'registration_date']