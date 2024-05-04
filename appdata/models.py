from django.db import models

# Create your models here.
class Department(models.Model):
    dname=models.CharField( max_length=50)
    loc=models.CharField( max_length=50)
    qr=models.CharField( max_length=500)
    