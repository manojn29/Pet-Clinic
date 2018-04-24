from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
	path('',views.about, name="about"),
	url(r'^appointment$', views.appointment, name="appointment"),
	path('about/',views.homepage, name="home"),
	path('blog/',views.blogs, name="blog"),
	path('contact/',views.contact, name='contact'),
	path('services/',views.services, name='services'),
	path('links/',views.links, name='links'),
	path('azar/',views.azar, name='azar'),
]