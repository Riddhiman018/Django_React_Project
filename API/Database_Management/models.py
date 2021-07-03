from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Userlist(models.Model):
    user_id = models.IntegerField()
    user_id.primary_key = True
    username = models.CharField(max_length=30)
    user_DOB = models.DateField(auto_now=False)
    user_pwd = models.CharField(max_length = 40)
    File_to_be_uploaded = models.FileField(upload_to='Cars_JPG')

