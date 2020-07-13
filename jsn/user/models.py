from django.db import models
from datetime import datetime
# Create your models here.
class Complaint(models.Model):  
    complaint_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    problem=models.CharField(max_length=40)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to="user/images/")
    address=models.TextField(max_length=1000)
    zip=models.CharField(max_length=15)
    ward=models.CharField(max_length=20)
    solved=models.BooleanField(default=False)
    date=models.DateField(default=datetime.today())
    class Meta: 
        db_table = "Complaint"  
    def __str__(self):
        if(self.solved):
            return (str(self.complaint_id)+'-'+'solved')
        else:
            return (str(self.complaint_id)+'-'+'unsolved')
            

