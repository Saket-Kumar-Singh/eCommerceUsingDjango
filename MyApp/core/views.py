from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    plc = "core\index.html"
    return render(request, plc)

def blank(request):
    return HttpResponse("Abhi immediate se nahi hai par banega")

# Create your views here.
