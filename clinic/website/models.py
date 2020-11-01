from django.db import models

class doctor(models.Model):
	doctorname=models.CharField(max_length=50)
	image=models.ImageField(null=True,blank=True)
	@property
	def imageurl(self):
		try:
			url=self.image.url
		except:
			url=''
		return url
	
	def __str__(self):
		return self.doctorname

class appointment(models.Model):
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	place=models.CharField(max_length=100)
	email=models.EmailField()
	date=models.DateTimeField(auto_now_add=True)
	doctor_name=models.ForeignKey(doctor,on_delete=models.CASCADE)
	
	class Meta:
		db_table="appointment"
	
	def __str__(self):
		return self.name
		
class contact(models.Model):
	s_name=models.CharField(max_length=50)
	place=models.CharField(max_length=50)
	email=models.CharField(max_length=100)
	message=models.TextField()
	
	class Meta:
		db_table="contact"
	
	def __str__(self):
		return self.s_name
