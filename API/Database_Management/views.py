from django.http.response import Http404
from django.shortcuts import render
from .serializier import User_JSON
from .models import Userlist
from rest_framework.decorators import api_view, parser_classes
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
import bcrypt
# Create your views here.

@api_view(['GET','POST'])
@parser_classes([JSONParser])
def UserSheet(request):
    if request.method == 'GET':
        try:
            Database = Userlist.objects.all()
            serializer = User_JSON(Database,many = True)
            return Response(serializer.data)
        except Userlist.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        salt = bcrypt.gensalt()
        byte_string = bytes(request.data['user_pwd'],'UTF-8') 
        request.data['user_pwd'] = bcrypt.hashpw(byte_string,salt).decode('UTF-8')
        serializer = User_JSON(data = request.data)
        print(request.data['user_pwd'])
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_validation_sheet(request):
    if request.method == 'POST':
        object_1 = Userlist.objects.get(user_id = request.data['user_id'])
        if object_1.user_pwd != request.data['user_pwd']:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status = status.HTTP_202_ACCEPTED)