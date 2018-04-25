from django.shortcuts import render
from .models import blog, contacts
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login/")
def homepage(request):
	return render(request, 'homepage/homepage.html')

@login_required(login_url="/accounts/login/")
def about(request):
	return render(request, 'homepage/about.html')

@login_required(login_url="/accounts/login/")
def blogs(request):
	blog1 = blog.objects.all()
	return render(request, 'homepage/blog.html', {'blog1': blog1})

@login_required(login_url="/accounts/login/")
def contact(request):
	docs = contacts.objects.all()
	return render(request, 'homepage/contact.html', {'docs': docs})

@login_required(login_url="/accounts/login/")
def services(request):
	return render(request, 'homepage/services.html')

@login_required(login_url="/accounts/login/")
def links(request):
	return render(request, 'homepage/links.html')

@login_required(login_url="/accounts/login/")
def appointment(request):
	form = forms.CreateAppoint(request.POST, request.FILES)
	return render(request, 'homepage/appointment.html', {'form':form})

def azar(request):
	return render(request, 'homepage/azhar.html')