from django.contrib import admin
from .models import StudentList

class StudentListAdmin(admin.ModelAdmin):
    list_display = ['roll', 'name','gender']
    list_editable = ['name']

admin.site.register(StudentList, StudentListAdmin)

