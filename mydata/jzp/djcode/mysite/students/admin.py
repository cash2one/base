from django.contrib import admin

from students.models import School, Student, Grade
# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Grade)
