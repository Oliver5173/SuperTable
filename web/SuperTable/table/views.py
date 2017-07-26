from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'home.html')

# def get_course(request):
#     year = request.GET['year']
#     semester = request.GET['semester']
#     course = request.GET['course']
#     courseNum = request.GET['courseNum']
#     rtnDict = {"year":year, "semester":semester, "course":course, "courseNum":courseNum}
#     return HttpResponse(rtnDict.values())

def get_course(request,year,semester,course,courseNum):
    rtnDict = {"year":year, "semester":semester, "course":course, "courseNum":courseNum}
    return HttpResponse(rtnDict.values())    
