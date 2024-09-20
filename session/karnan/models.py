from django.db import models

class userdata(models.Model):
    username= models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.PositiveIntegerField(max_length=12)
    

