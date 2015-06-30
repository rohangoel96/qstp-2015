
from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
	return render(request,"sujith/homepage.html")
def Page1(request):
	return render(request,"sujith/page1.html")
def Page2(request):
	return render(request,"sujith/page2.html")
# Create your views here.
