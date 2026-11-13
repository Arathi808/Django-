from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=50)
    mark=models.IntegerField()
    def __str__(self):
        return f'Student : {self.name}'