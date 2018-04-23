from django.db import models

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
		