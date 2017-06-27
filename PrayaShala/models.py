from django.db import models
from django.utils import timezone
from django.conf.urls.static import static
from django.conf import settings
class Institute(models.Model):
	Institute_Name=models.CharField(max_length=100)
	Email = models.CharField(max_length=100)
	Password = models.CharField(max_length=100)
	Key = models.CharField(default="",max_length=120)
	Varified=models.BooleanField(default=False )

class Faculty(models.Model):
	Email=models.CharField(max_length=100,default="")
	Name=models.CharField(max_length=100,default="")
	Area=models.CharField(max_length=100,default="")
	Experience=models.CharField(max_length=100,default="")
	Image=models.FileField(upload_to="Faculty_Profile",blank=True)

class Achivements(models.Model):
	Email=models.CharField(max_length=100,default="")
	Name=models.CharField(max_length=100,default="")
	Comment=models.CharField(max_length=200,default="")
	Image=models.FileField(upload_to="Achivements",blank=True)

class Students(models.Model):
	Institute_Email=models.CharField(max_length=100,default="")
	Student_Email=models.CharField(max_length=100,default="")
	Enrollment_No=models.IntegerField(default=0)
	Student_Name=models.CharField(max_length=100,default="")

class Blogs(models.Model):
	Email=models.CharField(max_length=100,default="")
	Title=models.CharField(max_length=100,default="")
	Author=models.CharField(max_length=100,default="")
	Text=models.TextField()
	published_date = models.DateTimeField(default=timezone.now)

class Tests(models.Model):
	Email=models.CharField(max_length=100,default="")
	Test_id=models.IntegerField(default=1)
	Test_Name=models.CharField(max_length=100,default="")
	publish_date=models.DateTimeField(default=timezone.now)
	No_of_Questions=models.IntegerField(default=0)
	Duration=models.IntegerField(default=0)
	Active=models.BooleanField(default=False)

class Questions(models.Model):
	Email=models.CharField(max_length=100,default="")
	Test_id=models.IntegerField(default=1)
	Question_No=models.IntegerField(default=1)
	Question=models.TextField(default="")
	Correct_Answers=models.TextField(default="")
	Wrong_Answers=models.TextField(max_length=100,default="")
	Type=models.CharField(max_length=100,default="")
	Image=models.FileField(upload_to="Questions",blank=True,null=True)
	Marks=models.IntegerField(default=0);
	Nmarks=models.IntegerField(default=0);

class Student_Record(models.Model):
	Student_Name=models.CharField(max_length=100)
	Email = models.CharField(max_length=100)
	Password = models.CharField(max_length=100)
	Key = models.CharField(default="",max_length=120)
	Varified=models.BooleanField(default=False )





