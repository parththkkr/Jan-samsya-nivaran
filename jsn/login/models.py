from django.db import models
from registration.models import Registration
# Create your models here.
class Login(models.Model):
    emailid=models.EmailField(default=None,primary_key=True)
    password=models.CharField(max_length=50)
    activeotp=models.BooleanField(default=False)
    lastlogin=models.CharField(max_length=30)
    otp=models.CharField(max_length=6)
    class Meta:     
        db_table = "Login"  
    def __str__(self):
        return self.emailid
