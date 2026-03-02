from django.contrib import admin
from .models import Student

# This makes the Student table visible in the admin panel
admin.site.register(Student)