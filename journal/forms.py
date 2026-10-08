from django import forms
from .models import Group
from .models import Student

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'group']