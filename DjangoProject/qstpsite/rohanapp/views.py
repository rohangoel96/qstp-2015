from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
	return render(request,"rohan/homepage.html")
def Page1(request):
	return render(request,"rohan/page1.html")
def Page2(request):
	return render(request,"rohan/page2.html")