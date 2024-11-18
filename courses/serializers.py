from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.ReadOnlyField(source='instructor.username')

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'instructor', 'instructor_name', 'created_at']
        read_only_fields = ['id', 'created_at', 'instructor_name']