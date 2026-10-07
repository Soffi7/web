from django.contrib import admin
from .models import Group, Student, Teacher, Subject, Grade, Attendance

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attendance)