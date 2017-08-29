from django.shortcuts import render
from django.http import HttpResponse
from .forms import courseForm
from django.views.decorators.csrf import csrf_protect

##from .models import Course


# Create your views here.

@csrf_protect 
def index(request):
    if request.method == "POST":
        form = courseForm(request.POST)
        if form.is_valid():
            info = {}
            info["year"] = form.cleaned_data["year"]
            info["semester"] = form.cleaned_data["semester"]
            info["content"] = form.cleaned_data["content"]
            return render(request,"index.html",info)
    else:
        return render(request,"index.html")
    

