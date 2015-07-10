from django.shortcuts import render,redirect
from django.http import HttpResponse

from rohanapp.models import LoginProfile,UserProfile

def Login(request): 
	login = ""
	if request.POST:
		username = request.POST['username']                                                                           
		password = request.POST['password']                                                                           
		utemp = LoginProfile.objects.get(username = username) 

		if utemp is not None:
			if utemp.password == password:
				login = "Success"
				request.session['username'] = username
				return redirect(LoginSuccess,permanent=True)
			else:
				login = "Wrong Password"
	
	context = {'login': login}
	return render(request,"rohan/login.html",context)                                                                 
	


def LoginSuccess(request):
	username = str(request.session['username'])
	user_list = UserProfile.objects.filter(username = username)
	
 	name = user_list[0].name
	
	context = {'name' : name}
	return render(request,"rohan/login_success.html",context) 


def EditProfile(request):
	login = ""
	if request.POST:
		username = request.POST['username']                                                                           
		old_password = request.POST['old_password']
		new_password = request.POST['new_password']                                                                           
		
		utemp = LoginProfile.objects.get(username = username) 

		if utemp is not None:
			if utemp.password == old_password:
				utemp.password = new_password
				utemp.save()
				login = "Passowrd Successfully Updated"
			else:
				login = "Wrong Password"

	context = {'login': login}
	return render(request,"rohan/edit_profile.html",context) 



		   
def Page1(request):                                                                                                   
	return render(request,"rohan/page1.html")                                                                    

def Page2(request):                                                                                                   
	return render(request,"rohan/page2.html") 