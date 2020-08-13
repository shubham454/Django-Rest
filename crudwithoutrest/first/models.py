from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    marks = models.FloatField()
    addr = models.CharField(max_length=20)
