from django.shortcuts import render
from django.http import HttpResponse

from rohanapp.models import LoginProfile

def Login(request): 
	login = ""
	if request.POST:
		username = request.POST['username']                                                                           
		password = request.POST['password']                                                                           
		utemp = LoginProfile.objects.get(username = username) 

		if utemp is not None:
			if utemp.password == password:
				login = "Success"
			else:
				login = "Wrong Password"
	
	context = {'login': login}
	return render(request,"rohan/login.html",context)                                                                 
	       
		   
		   
def Page1(request):                                                                                                   
	return render(request,"rohan/page1.html")                                                                    

def Page2(request):                                                                                                   
	return render(request,"rohan/page2.html") 