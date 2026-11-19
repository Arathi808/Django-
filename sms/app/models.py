from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return f'Course: {self.name}'
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='student')
    mark=models.IntegerField()
    def __str__(self):
        return f'Student : {self.name}'

