from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail

def home(request):
	return render(request,'base.html')
def message(request):
	con=conform()
	if request.method=='POST':
		form=conform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/confirm/')
	context={'form':con}
	return render(request,'msg.html',context)
def appointments(request):
	appo=appform()
	subject="confirmation email"
	body='''sir/madam,
	Your booking has been confirmed.our staff will contact you for confirming your date.thank you!!!'''	
	if request.method=='POST':
		form=appform(request.POST)
		if form.is_valid():
			to=form.cleaned_data['email']
			form.save()
			send_mail(subject,body,"sender@gmail.com",[to],fail_silently=False)
			return redirect('/success/')
	context={'form':appo}
	return render(request,'appoint.html',context)
def success(request):
	return render(request,'success.html')
def confirm(request):
	return render(request,'confirm.html')