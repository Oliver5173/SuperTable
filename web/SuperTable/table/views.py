# pylint: disable=C0103,C0111, W0611
import re
import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# import re and forms for course
from django.views.decorators.cache import cache_page
from .forms import SearchForm
from .models import SearchRequest


@cache_page(60)
def index(request):
    yearList = ["2017", "2018"]
    semseterList = ["Spring", "Summer", "Fall"]
    preferenceList = ["All", "Morning", "Afternoon"] #,"Compact","Loose"]
    infoDict = {"yearList":yearList, "semseterList":semseterList, "preferenceList":preferenceList}
    return render(request, 'home.html', {"infoDict":infoDict})


def get_course(request):
    rtnList = []
    if request.POST:
        year = request.POST.get('year', None)
        semester = request.POST.get('semester', None)
        courseList = request.POST.get('courseList', None)
        preference = request.POST.get('preference', None)
        courseList = courseList.split(";")
        rtnDict = {}
        courseTimes = 0
        for course in courseList:
            match = re.match(r'([a-z]+)([0-9]+)', course, re.I).groups()
            department = match[0]
            courseNum = match[1]

            subRequest = SearchRequest(year, semester, preference, department, courseNum,courseTimes)
            courseTimes = subRequest.courseTimes + 1
            rtnDict.update(subRequest.get_rtnVal())

    return render(request, 'result.html', {"rtnDict":json.dumps(rtnDict).replace('"',r"\"")})
   
