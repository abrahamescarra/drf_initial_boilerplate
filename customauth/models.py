from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    char_field=models.CharField(max_length=100,null=True,blank=True)
    image_field=models.ImageField(upload_to='company/logo',null=True)