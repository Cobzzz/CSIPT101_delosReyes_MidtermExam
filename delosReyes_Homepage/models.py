from django.db import models

# Create your models here.

class cInfos(models.Model):
    cInfo=models.SmallIntegerField
    cName=models.TextField(max_length=250)
    cAge=models.SmallIntegerField
    cID=models.CharField(max_length=100)
    cDepartment=models.TextField(max_length=200)
