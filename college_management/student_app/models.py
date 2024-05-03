from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=900)
    Age=models.IntegerField()
    Address=models.CharField(max_length=900)
    Gender=models.CharField(max_length=900)
    DOB=models.DateField()
    Photo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.Name
    

