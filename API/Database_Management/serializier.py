from collections import UserDict

from rest_framework import serializers 
from .models import Userlist

class User_JSON(serializers.ModelSerializer):
    user_pwd = serializers.CharField(
        style = {'input type':'password'}
    )
    
    class Meta:
    
        model = Userlist
    
        fields = ('user_id','username','user_DOB','user_pwd')