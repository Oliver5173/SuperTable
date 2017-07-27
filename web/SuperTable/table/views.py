from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# import re and forms for course
import re
from .forms import SearchForm
from .models import SearchRequest
from django.views.decorators.cache import cache_page

@cache_page(60*15)
def index(request):
    yearList = [2017,2018]
    semseterList = ["Spring","Summer","Fall"]
    infoDict = {"yearList":yearList,"semseterList":semseterList}
    return render(request,'home.html', {"infoDict":infoDict})


def get_course(request):
    if request.POST:
        year = request.POST.get('year',None)
        semester = request.POST.get('semester',None)
        courseList = request.POST.get('courseList',None)
        courseList = courseList.split(";")
        rtnDict = {"year":year, "semester":semester, "courseList":courseList}
    return render(request, 'result.html', {"rtnDict":rtnDict})    
