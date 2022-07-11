from rest_framework import serializers
from .models import *

class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Model1

class Model2Serializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Model2