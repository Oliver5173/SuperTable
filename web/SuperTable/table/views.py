from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request,'home.html')


def get_course(request,year,semester,courseList):
    courses = courseList.split(";")
    rtnDict = {"year":year, "semester":semester, "course":courses}
    return HttpResponse(rtnDict.values())    
