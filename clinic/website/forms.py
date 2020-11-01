from django import forms
from .models import *

class appform(forms.ModelForm):
	class Meta:
		model=appointment
		fields=['name','age','place','email','doctor_name']
		
class conform(forms.ModelForm):
	class Meta:
		model=contact
		fields="__all__"