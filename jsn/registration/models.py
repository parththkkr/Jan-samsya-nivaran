from django.db import models

# Create your models here.

class Registration(models.Model):  
    
    firstname=models.CharField(max_length=20,default=None)
    lastname=models.CharField(max_length=20,default=None)
    username=models.CharField(max_length=20,default=None)
    emailid=models.EmailField(default=None,primary_key=True)
    password=models.CharField(max_length=50,default=None)
    city=models.CharField(max_length=20,default=None)
    state=models.CharField(max_length=20,default=None)
    zipcode=models.CharField(max_length=20,default=None)
    aggrement=models.BooleanField(default=False)
    class Meta: 
        db_table = "Registration"  
    def __str__(self):
        return self.username
