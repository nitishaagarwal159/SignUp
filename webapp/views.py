from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from webapp.forms import User_Signup
from . models import users
from . serializers import usersSerializer
from django.contrib.auth.models import User

class userList(APIView):
    def get(self,request):
        #pass
        user1=users.objects.all()
        serializer=usersSerializer(user1,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def signup(request):
    if request.method=='POST':
        form=User_Signup(request.POST)
    if form.is_valid():
        password=form.cleaned_data['password']
        user = User.objects.create_user(password)
        return redirect('blog')
    else:
        return HttpResponse('Enter correct format')
