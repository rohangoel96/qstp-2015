from django.shortcuts import render
from django.http import HttpResponse

from rohanapp.models import LoginProfile

def Login(request):                                                                                                   
	username = request.POST['username']                                                                           
	password = request.POST['password']                                                                           
	login=""

	utemp = LoginProfile.objects.get(username = username) 

	if utemp is not None:
		if utemp.password == password:
			login = "Success"
	else:
		login = "User not found"

	context = {'login': login}

	
	return render(request,"rohan_templates/login.html",context)                                                                 
	       
def Page1(request):                                                                                                   
	return render(request,"rohan_templates/page1.html")                                                                    

def Page2(request):                                                                                                   
	return render(request,"rohan_templates/page2.html") 