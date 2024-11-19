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

    def __str__(self) -> str:
        return self.name

    @property
    def age(self) -> int:
        from datetime import date
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return 0