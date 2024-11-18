from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="student_profile"
    )
    name = models.CharField(max_length=100)
    dob = models.DateField("Date of Birth", null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name