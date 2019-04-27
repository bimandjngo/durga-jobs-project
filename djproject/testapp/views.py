from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request, "testApp/index.html")

def hydjobs1(request):
    job_list = hydjobs.objects.order_by('date')
    my_dict = {'job_list' : job_list}
    return render(request, 'testApp/hydjobs.html', context = my_dict)

def bangalorejobs1(request):
    return render(request, 'testApp/bangalorejobs.html', context = my_dict)

def chennaijobs1(request):
    return render(request, 'testApp/chennaijobs.html', context = my_dict)

def punejobs1(request):
    job_list = punejobs.objects.order_by('company')
    my_dict = {'job_list' : job_list}
    return render(request, 'testApp/punejobs.html', context = my_dict)
