from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dob', 'registration_date')
    search_fields = ('name', 'user__email')
    list_filter = ('registration_date',)
    ordering = ('name',)

admin.site.register(Student, StudentAdmin)