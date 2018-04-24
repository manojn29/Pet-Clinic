from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
	url(r'^$',views.about, name="about"),
	url(r'^appointment/$', views.appointment, name="appointment"),
	url(r'^about/$',views.homepage, name="home"),
	url(r'^blog/$',views.blogs, name="blog"),
	url(r'^contact/$',views.contact, name='contact'),
	url(r'^services/$',views.services, name='services'),
	url(r'^links/$',views.links, name='links'),
	url(r'^azar/$',views.azar, name='azar'),
]