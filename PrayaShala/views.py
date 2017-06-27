from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.contrib.auth.hashers import make_password
from random import randint
from django.core.mail import send_mail
from django.utils import timezone



def index(request):
	return render(request,'PrayaShala/index.html',{})
def institute(request):
	return render(request,'PrayaShala/Institute.html',{})

def ISignup(request):
	if request.method=='POST':
			name=request.POST['Name']
			email=request.POST['Email']
			password=request.POST['Password']
			if Institute.objects.filter(Email=email).exists():
				return HttpResponse('Email id already register')
			else:
				key=make_password(email,"ravikiradoo")
				newpassword=make_password(password,"ravikiradoo")
				message="http://127.0.0.1:8000/activeI/"+key
				data=Institute(Institute_Name=name,Email=email,Password=newpassword,Key=key)
				send_mail(
					'PrayaShala',
					message,
					"kiradooravi@gmail.com",
					[email]

					)
				data.save()

				return HttpResponse('pass')

def Student_Signup(request):
	if request.method=='POST':
			name=request.POST['Name']
			email=request.POST['Email']
			password=request.POST['Password']
			if Student_Record.objects.filter(Email=email).exists():
				return HttpResponse('Email id already register')
			else:
				key=make_password(email,"ravikiradoo")
				newpassword=make_password(password,"ravikiradoo")
				message="http://127.0.0.1:8000/activeS/"+key
				data=Student_Record(Student_Name=name,Email=email,Password=newpassword,Key=key)
				send_mail(
					'PrayaShala',
					message,
					"kiradooravi@gmail.com",
					[email]

					)
				data.save()

				return HttpResponse('pass')

def activeS(request,key):
	ins=Student_Record.objects.get(Key=key)
	ins.Varified=True
	ins.save()
	return HttpResponse("thanks")

def Student_Login(request):
	if request.method=='POST':
			email=request.POST['Email']
			password=request.POST['Password']
			newpassword=make_password(password,"ravikiradoo")
			if Student_Record.objects.filter(Email=email,Password=newpassword,Varified=False).exists():
				return HttpResponse('fail1')
			elif Student_Record.objects.filter(Email=email,Password=newpassword,Varified=True).exists():
				return HttpResponse('pass')
			else:
				return HttpResponse("fail2")

def StudentHome(request):
	if request.method=='POST':
		email=request.POST['email']
		dataS=Student_Record.objects.get(Email=email)
		dataI=Institute.objects.all()
		return render(request,"PrayaShala/StudentHome.html",{'dataS':dataS,'dataI':dataI})
	else:
		return HttpResponse("Error")


def CLogin(request):
	if request.method=='POST':
			email=request.POST['Email']
			password=request.POST['Password']
			newpassword=make_password(password,"ravikiradoo")
			if Institute.objects.filter(Email=email,Password=newpassword,Varified=False).exists():
				return HttpResponse('fail1')
			elif Institute.objects.filter(Email=email,Password=newpassword,Varified=True).exists():
				return HttpResponse('pass')
			else:
				return HttpResponse("fail2")




def activeI(request,key):
	ins=Institute.objects.get(Key=key)
	ins.Varified=True
	ins.save()
	return HttpResponse("thanks")

def ILogin(request):
	if request.method=='POST':
		email=request.POST['email']
		data=Institute.objects.get(Email=email)
		dataT=Tests.objects.filter(Email=email)
		return render(request,"PrayaShala/InstituteHome.html",{'data':data,'dataT':dataT})
	else:
		return HttpResponse("Please Login ")

def IHome(request):
	if request.method=='POST':
		email=request.POST['email']
		data=Institute.objects.get(Email=email)
		return render(request,"PrayaShala/InstituteHome.html",{'data':data})
	else:
		return HttpResponse("Error")

def IFaculty(request):
	if request.method=="POST":
		dataI=''
		dataF=''
		email=request.POST['email']
		if Faculty.objects.filter(Email=email).exists():
			dataF=Faculty.objects.filter(Email=email)
		if Institute.objects.filter(Email=email).exists():
			dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Faculty.html",{'dataI':dataI,'dataF':dataF,"Email":email})
		
def AddFacultyProfile(request):
	if request.method=="POST":
		email=request.POST['email']
		name=request.POST['name']
		Area=request.POST['Area']
		Exp=request.POST['Exp']
		image=request.FILES['Image']
		data=Faculty(Email=email,Name=name,Area=Area,Experience=Exp,Image=image)
		data.save()
		dataF=Faculty.objects.filter(Email=email)
		dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Faculty.html",{'dataI':dataI,'dataF':dataF,"Email":email})

def IAchive(request):
	if request.method=="POST":
		dataI=''
		dataA=''
		email=request.POST['email']
		if Faculty.objects.filter(Email=email).exists():
			dataA=Achivements.objects.filter(Email=email)
		if Institute.objects.filter(Email=email).exists():
			dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Achivements.html",{'dataI':dataI,'dataA':dataA,"Email":email})

def SAchive(request):
	if request.method=="POST":
		dataI=''
		dataA=''
		email1=request.POST['email1']
		email2=request.POST['email2']
		if Achivements.objects.filter(Email=email1).exists():
			dataA=Achivements.objects.filter(Email=email1)
		dataI=Institute.objects.get(Email=email1)
		dataS=Student_Record.objects.get(Email=email2)
		return render(request,"PrayaShala/achivements.html",{'dataI':dataI,'dataA':dataA,"dataS":dataS})

def AddAchivements(request):
	if request.method=="POST":
		email=request.POST['email']
		name=request.POST['name']
		comment=request.POST['comment']
		image=request.FILES['Image']
		data=Achivements(Email=email,Name=name,Comment=comment,Image=image)
		data.save()
		dataA=Achivements.objects.filter(Email=email)
		dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Achivements.html",{'dataI':dataI,'dataA':dataA,"Email":email})

def IStudents(request):
	if request.method=="POST":
		dataI=''
		dataS=''
		email=request.POST['email']
		if Students.objects.filter(Institute_Email=email).exists():
			dataS=Students.objects.filter(Institute_Email=email)
		if Institute.objects.filter(Email=email).exists():
			dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Students.html",{'dataI':dataI,'dataS':dataS,"Email":email})

def AddStudents(request):
	if request.method=="POST":
		email=request.POST['Iemail']
		name=request.POST['name']
		Semail=request.POST['Semail']
		Enrollment=request.POST['Enrollment']
		data=Students(Institute_Email=email,Student_Email=Semail,Student_Name=name,Enrollment_No=Enrollment)
		data.save()
		dataS=Students.objects.filter(Institute_Email=email)
		dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Students.html",{'dataI':dataI,'dataS':dataS,"Email":email})

def IBlog(request):
	if request.method=="POST":
		dataI=''
		dataB=''
		email=request.POST['email']
		if Blogs.objects.filter(Email=email).exists():
			dataB=Blogs.objects.filter(Email=email)
		if Institute.objects.filter(Email=email).exists():
			dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Blogs.html",{'dataI':dataI,'dataB':dataB,"Email":email})

def AddBlogs(request):
	if request.method=="POST":
		email=request.POST['email']
		title=request.POST['Title']
		author=request.POST['Author']
		text=request.POST['Text']
		data=Blogs(Email=email,Title=title,Author=author,Text=text)
		data.save()
		dataB=Blogs.objects.filter(Email=email)
		dataI=Institute.objects.filter(Email=email)
		return render(request,"PrayaShala/Blogs.html",{'dataI':dataI,'dataB':dataB,"Email":email})

def GoToTest(request):
	if request.method=="POST":
		email=request.POST['email']
		return render(request,"PrayaShala/CreateTest.html",{'Email':email})

def AddTest(request):
	if request.method=="POST":
		email=request.POST['email']
		Test_name=request.POST['testname']
		Test_id=request.POST['testid']
		date=request.POST['date']
		time=request.POST['time']
		datetime=date+" "+time
		duration=request.POST["duration"]
		if Tests.objects.filter(Email=email,Test_id=Test_id):
			return HttpResponse("fail")
		else:
			data=Tests(Email=email,Test_Name=Test_name,Test_id=Test_id,publish_date=datetime,Duration=duration)
			data.save()
			return HttpResponse("pass")

def QuestionsPage(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		dataT=Tests.objects.filter(Email=email,Test_id=testid)
		return render(request,"PrayaShala/Question.html",{"TS":testid,"Email":email})
		

		
def Edit_Question(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		qno=request.POST['qno']
		dataT=Tests.objects.filter(Email=email,Test_id=testid)
		dataQ=Questions.objects.filter(Email=email,Test_id=testid,Question_No=qno)
		return render(request,"PrayaShala/Edit_Question.html",{"TS":testid,"Email":email,"dataQ":dataQ})



def AddQuestion(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		que=request.POST['Question']
		queno=request.POST['QuestionNo']
		ca=request.POST['CA']
		wa=request.POST['WA']
		marks=request.POST['marks']
		nmarks=request.POST['Nmarks']
		c1=request.POST['c1']
		type=request.POST['type']
		image=''
		if c1=="yes":
			image=request.FILES['image']

		
		if Questions.objects.filter(Email=email,Test_id=testid,Question_No=queno).exists():
			Questions.objects.filter(Email=email,Test_id=testid,Question_No=queno).delete()

		data=Questions(Email=email,Test_id=testid,Question=que,Correct_Answers=ca,Wrong_Answers=wa,Type=type,Marks=marks,Nmarks=nmarks
			,Image=image,Question_No=queno)
		data.save()

		dataQ=Questions.objects.filter(Email=email,Test_id=testid)

		data=Tests.objects.get(Email=email,Test_id=testid)
		data.No_of_Questions=data.No_of_Questions+1
		data.save()
		return render(request,"PrayaShala/Question.html",{"TS":testid,"Email":email,"dataQ":dataQ})

def instituteHome(request):
	if request.method=="POST":
		email1=request.POST['email']
		email2=request.POST['Email']
		dataI=Institute.objects.get(Email=email1)
		dataS=Student_Record.objects.get(Email=email2)
		dataT=Tests.objects.filter(Email=email1)
		return render(request,'PrayaShala/instituteHome.html',{'dataI':dataI,'dataS':dataS,'dataT':dataT})
		
		



def SFaculty(request):
	if request.method=="POST":
		dataI=''
		dataF=''
		email=request.POST['email1']
		Email=request.POST['email2']

		if Faculty.objects.filter(Email=email).exists():
			dataF=Faculty.objects.filter(Email=email)
		
		dataI=Institute.objects.get(Email=email)
		dataS=Student_Record.objects.get(Email=Email)
		return render(request,"PrayaShala/faculty.html",{'dataI':dataI,'dataF':dataF,"dataS":dataS})

		
def SBlog(request):
	if request.method=="POST":
		dataI=''
		dataB=''

		email1=request.POST['email1']
		email2=request.POST['email2']
		if Blogs.objects.filter(Email=email1).exists():
			dataB=Blogs.objects.filter(Email=email1)
		dataS=Student_Record(Email=email2)
		dataI=Institute.objects.get(Email=email1)
		return render(request,"PrayaShala/blogs.html",{'dataI':dataI,'dataB':dataB,'dataS':dataS})


def OpenTest(request):
	if request.method=="POST":
		email1=request.POST['email1']
		email2=request.POST['email2']
		testid=request.POST['testid']
		dataQ=Questions.objects.filter(Email=email1,Test_id=testid)
		dataT=Tests.objects.get(Email=email1,Test_id=testid)
		return render(request,"PrayaShala/QuestionPaper.html",{'dataQ':dataQ,'dataT':dataT,"Email":email2})

def FetchPaper(request):
	if request.method=="POST":
		email=request.POST['email']
		testid=request.POST['testid']
		Qno=request.POST['QN']
		dataQ=Questions.objects.get(Email=email,Test_id=testid,Question_No=Qno)
		Image="";
		if dataQ.Image:
			Image=dataQ.Image.url;
		
		data={
		"Question_No":dataQ.Question_No,
		"Question":dataQ.Question,
		"Wrong_Answers":dataQ.Wrong_Answers,
		"Correct_Answers":dataQ.Correct_Answers,
		"Type":dataQ.Type,
		"Marks":dataQ.Marks,
		"Nmarks":dataQ.Nmarks,

		"Image":Image,
		}
		return JsonResponse(data)

def Resume(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		dataT=Tests.objects.filter(Email=email,Test_id=testid)
		dataQ=Questions.objects.filter(Email=email,Test_id=testid)
		return render(request,"PrayaShala/Question.html",{"TS":testid,"Email":email,"dataQ":dataQ})



def DeleteTest(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		Tests.objects.get(Email=email,Test_id=testid).delete()
		Questions.objects.filter(Email=email,Test_id=testid).delete()
		return HttpResponse("Test Deleted Successfully")

def DeleteBlog(request):
	if request.method=="POST":
		pk=request.POST['pk']
		Blogs.objects.get(pk=pk).delete()
		return HttpResponse("Blog Deleted Successfully")

def ActiveTest(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		data=Tests.objects.get(Email=email,Test_id=testid)
		data.Active=True
		data.save()
		return HttpResponse("Test Published Successfully")
def DeActiveTest(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		data=Tests.objects.get(Email=email,Test_id=testid)
		data.Active=False
		data.save()
		return HttpResponse("Test Deactivated Successfully")

def Edit_Test(request):
	if request.method=="POST":
		testid=request.POST['testid']
		email=request.POST['email']
		data=Tests.objects.get(Email=email,Test_id=testid)
		return render(request,"PrayaShala/EditTest.html",{"Tests":data})


def EditTest(request):
	if request.method=="POST":
		email=request.POST['email']
		Test_name=request.POST['testname']
		Test_id=request.POST['testid']
		date=request.POST['date']
		time=request.POST['time']
		datetime=date+" "+time
		duration=request.POST["duration"]
		
		data=Tests.objects.get(Email=email,Test_id=Test_id)
		data.Test_Name=Test_name
		data.publish_date=datetime
		data.Duration=duration

		data.save()
		return HttpResponse("Test Edited Successfully")

def Preview(request):
	if request.method=="POST":
		email=request.POST['email']
		testid=request.POST['testid']
		data=Questions.objects.filter(Email=email,Test_id=testid)
		return render(request,"PrayaShala/Preview.html",{"data":data})