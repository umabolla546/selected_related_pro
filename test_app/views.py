from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def home_view(request):
    return HttpResponse("<h2>hello home page</h2>")