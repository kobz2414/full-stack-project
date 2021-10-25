from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    semester = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)