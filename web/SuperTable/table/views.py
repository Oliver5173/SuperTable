# pylint: disable=C0103,C0111

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# import re and forms for course
import re
from .forms import SearchForm
from .models import SearchRequest
from django.views.decorators.cache import cache_page

@cache_page(60*15)
def index(request):
    yearList = ["2017", "2018"]
    semseterList = ["Spring", "Summer", "Fall"]
    preferenceList = ["All", "Morning", "Afternoon"] #,"Compact","Loose"]
    infoDict = {"yearList":yearList, "semseterList":semseterList, "preferenceList":preferenceList}
    return render(request, 'home.html', {"infoDict":infoDict})


def get_course(request):
    if request.POST:
        year = request.POST.get('year', None)
        semester = request.POST.get('semester', None)
        courseList = request.POST.get('courseList', None)
        preference = request.POST.get('preference', None)
        courseList = courseList.split(";")
        for course in courseList:
            match = re.match(r'([a-z]+)([0-9]+)', course, re.I).groups()
            department = match[0]
            courseNum = match[1]

            subRequest = SearchRequest(year, semester, preference, department, courseNum)
            rtnDict = subRequest.get_rtnVal()

        # rtnDict = {"year":year, "semester":semester, "courseList":courseList}
    return render(request, 'result.html', {"rtnDict":rtnDict})    
