from django.shortcuts import render
from .fibonacci import find_fibonacci as ff

def home(request):
    fibonacci = ff()
    return render(request,'index.html',{'param1':fibonacci})
# Create your views here.
