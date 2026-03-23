from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    course_choices = [
        ('DS', 'Data Science'),
        ('DA', 'Data Analyst'),
        ('FSD', 'Full Stack Development'),
        ('WD', 'Web Development'),
        ('DM', 'Digital Marketing'),
    ]
    course_name = models.CharField(max_length=3, choices=course_choices)

    def __str__(self):
        return self.name
