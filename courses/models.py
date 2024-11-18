from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="courses"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name