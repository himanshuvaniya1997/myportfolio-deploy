from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')	

def skill(request):
	return render(request,'skill.html')		

def portfolio(request):
	return render(request,'portfolio.html')	

def contact(request):
	return render(request,'contact.html')	

def project(request):
	return render(request,'project.html')	

def photos(request):
	return render(request,'photos.html')			

def contact_data(request):
	if request.method=="POST":
		User.objects.create(
		    name=request.POST['name'],		
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message'],		
			)
		msg="Send message successfully"
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')
			
			
