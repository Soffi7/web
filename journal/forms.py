from django import forms
from .models import Group, Student, Grade, Teacher, Subject

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'comment']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'group']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'value', 'date']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'teachers']