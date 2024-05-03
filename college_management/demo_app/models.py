from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# abstract class
class Master(models.Model):
    created_user=models.ForeignKey(User,on_delete=models.CASCADE ,limit_choices_to={'is_staff':True})
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True , verbose_name="Active")


class New_State(Master):
    statename=models.CharField(max_length=300,verbose_name="State Name")

    def __str__(self):
        return self.statename
class District(Master):
    state = models.ForeignKey(New_State, on_delete=models.CASCADE)
    districtname = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.districtname
    

gender_choice=(
    ("male","Male"),
    ("Female","Female")
) 
class Student_gender(Master):
    StudentName=models.CharField(max_length=200)
    
    student_details=models.CharField(max_length=900,choices=gender_choice)

