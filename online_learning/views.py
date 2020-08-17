from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.models import User
from django.http import HttpResponse
from teacher.models import Teacher_Registration 
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from teacher.models import Teacher_Registration  
from courses.models import course_registration,course_count 



from django.conf import settings
 
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

 
def teacher_registration(request):
	return render(request,"teacher_registration.html") 
def message(request):
	return render(request,"message.html") 
def teacher_details(request):
	return render(request,"teacher_details.html") 

 


def upload_course(request):
		if request.method == 'POST':
			cname= request.POST.get('cname','')
			temail= request.POST.get('temail','')
			cdiscription= request.POST.get('cdiscription','')
			cphoto= request.FILES['cphoto'];
			cfile= request.FILES['cfile'];
			tpassword= request.POST.get('tpassword','')
			ccategory= request.POST.get('ccategory','')

			teachers_verify=Teacher_Registration.objects.all()
			for t in teachers_verify:
				if t.email ==temail and t.password==tpassword:
					if t.selection==True:
						x=course_registration(teacher_name=t.name,teacher_designation=t.designation,teacher_profile_photo=t.profile_photo,cname=cname,cdiscription=cdiscription,cphoto=cphoto,cfile=cfile,temail=temail,tpassword=tpassword,ccategory=ccategory)
						x.save()
						return render(request,"message.html",{'message':"Course Successfully Added  ...!"}) 
					else:
						return render(request,"message.html",{'message':" Sorry You Are Not Yet  to Selected  for the ADMIN so wait for selection...!"}) 
				else:
					pass
			return render(request,"message.html",{'message':"Invalid Email and Password Or Please Create New Account"}) 

				
		else:
			return redirect('new_course')


  
def insert(request):
		if request.method == 'POST':
			name= request.POST.get('name','')
			email= request.POST.get('email','')
			designation= request.POST.get('designation','')
			profile_photo= request.FILES['profile_photo'];
			password= request.POST.get('password','')
			about= request.POST.get('about','')
			work_exp= request.POST.get('work_exp','')
			if Teacher_Registration.objects.filter(email=email).exists():
				return render(request,"message.html",{'message':"Email Already Exists Try New One!"}) 
			else:
				x=Teacher_Registration(name=name,email=email,designation=designation,profile_photo=profile_photo,password=password,about=about,work_exp=work_exp)
				x.save()
				return render(request,"message.html",{'message':"Teacher Request Submitted  ...!"}) 
		return render(request,"teacher_registration.html") 
							

def index(request):
	w=s=b=sc=sm=0
	c_count=course_registration.objects.all()
	for c in c_count:
		if c.ccategory == "civil_services":
			sc+=1
		elif c.ccategory == "soft_dev":
			s+=1
		elif c.ccategory  == "banking":
			b+=1
		elif c.ccategory == "web_dev":
			w+=1
		else:
			sm+=1


	submit=course_count.objects.get(id=5)
	submit.web_dev=w
	submit.soft_dev=s
	submit.banking=b
	submit.social_media=sm
	submit.civil_services=sc
	
	# print("web_dev=",w)
	submit.save()
	return render(request,"index.html",{'web_dev':w,'soft_dev':s,'banking':b,'civil_services':sc,'social_media':sm}) 


def news(request):
	return render(request,"blog.html") 
def elements(request):
	return render(request,"elements.html") 
def contact(request):
	return render(request,"contact.html")
def new_course(request):
	return render(request,"new_course.html")
def courses(request):
	courses_info=course_registration.objects.all()
	return render(request,"courses.html",{'courses_info':courses_info,'media_url':settings.MEDIA_URL})

	
