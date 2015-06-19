from django.shortcuts import render
from django.http import HttpResponse

def welcomePage(request):
	return render(request,'AnmolApp/welcomepage.html')

def animelist(request):
	return render(request,'AnmolApp/animelist.html')
	
def homePage(request):
	if request.POST:
		request.session['your_name'] = request.POST['your_name']
	context = {'your_name':request.session['your_name']}
	return render(request,'AnmolApp/homepage.html',context)
	
def about(request):
	context = {'your_name':request.session['your_name']} 
	return render(request,'AnmolApp/about.html',context)
	
def snk(request):
	return render(request,'AnmolApp/snk.html')
	
def tgre(request):
	return render(request,'AnmolApp/tgre.html')

# Create your views here.
