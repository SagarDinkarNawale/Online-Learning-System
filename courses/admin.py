from django.contrib import admin
from .models import course_registration,course_count
# Register your models here.
admin.site.register(course_registration)
admin.site.register(course_count)