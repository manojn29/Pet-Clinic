from django.shortcuts import render
from .models import blog, contacts
# Create your views here.
def homepage(request):
	return render(request, 'homepage/homepage.html')

def about(request):
	return render(request, 'homepage/about.html')

def blogs(request):
	blog1 = blog.objects.all()
	return render(request, 'homepage/blog.html', {'blog1': blog1})

def contact(request):
	docs = contacts.objects.all()
	return render(request, 'homepage/contact.html', {'docs': docs})

def services(request):
	return render(request, 'homepage/services.html')

def links(request):
	return render(request, 'homepage/links.html')

def azar(request):
	return render(request, 'homepage/azhar.html')