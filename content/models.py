from django.db import models
from customauth.models import CustomUser

class Model1(models.Model):
    #Strings
    char_field=models.CharField(max_length=50)
    #Dates
    date_field=models.DateField()
    #Files
    file_field=models.FileField( upload_to="path",null=True)

    #if necessary
    #owner=models.ForeignKey(CustomUser,related_name='models', on_delete=models.CASCADE,null=True)

class Model2(models.Model):
    char_field=models.CharField(max_length=50)
    truck=models.ForeignKey(Model1, on_delete=models.CASCADE)
    
    #if necessary
    #owner=models.ForeignKey(CustomUser,related_name='models2', on_delete=models.CASCADE,null=True)