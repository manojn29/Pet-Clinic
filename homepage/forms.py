from django import forms
from . import models

class CreateAppoint(forms.ModelForm):
	class Meta:
		model = models.appoint
		fields = ['uemail','pet']