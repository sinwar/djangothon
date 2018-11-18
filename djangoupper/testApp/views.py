import os
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
# from pydot import pyparsing
from testApp.models import UserModel
# Create your views here.


def my_view(request):
    if (request.method=="GET"):
        r = subprocess.call("manage.py graph_models -a -X LogEntry,Session,AbstractBaseSession,User,Group,AbstractUser,Permission,ContentType > my_project.dot", shell=True)
        print(r)
        file = open('my_project.dot', 'r')#READING DOT FILE
        text=file.read()
        return HttpResponse(text)
    