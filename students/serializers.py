from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'name', 'dob', 'registration_date']
        read_only_fields = ['id', 'registration_date']

    def validate_name(self, value: str) -> str:
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно содержать не менее 2 символов.")
        return value

    def validate_dob(self, value):
        from datetime import date
        if value and value > date.today():
            raise serializers.ValidationError("Дата рождения не может быть в будущем.")
        return value