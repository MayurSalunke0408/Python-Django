from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'number', 'email', 'gender', 'course_name']
        widgets = {
            'gender': forms.Select(choices=Student.gender_choices),
            'course_name': forms.Select(choices=Student.course_choices),
        }