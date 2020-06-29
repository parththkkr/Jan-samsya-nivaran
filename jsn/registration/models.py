from django.db import models

# Create your models here.

class Registration(models.Model):  
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    emailid=models.EmailField(default=None)
    password=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=20)
    aggrement=models.BooleanField(default=False)
    class Meta: 
        db_table = "Registration"  
    def __str__(self):
        return self.username
