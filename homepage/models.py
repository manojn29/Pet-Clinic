from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
	head = models.CharField(max_length = 100)
	body = models.TextField()

	def __str__(self):
		return self.head 

	def snippet(self):
		return self.body[:50] + "..."


class contacts(models.Model):
	name = models.CharField(max_length = 20)
	spec = models.CharField(max_length = 25)
	email = models.EmailField()
	phone = models.IntegerField()

	def __str__(self):
		return self.name
		

class appoint(models.Model):
	uemail = models.EmailField()
	pet = models.CharField(max_length = 25)
	
"""
class appoint2(models.Model):
	author = models.ForeignKey(User, default=None, on_delete=models.CASCADE,)
"""