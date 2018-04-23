from django.contrib import admin
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
	path('',views.homepage, name="home"),
	path('about/',views.about, name="about"),
	path('blog/',views.blogs, name="blog"),
	path('contact/',views.contact, name='contact'),
	path('services/',views.services, name='services'),
	path('links/',views.links, name='links'),
]