# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from  .models import Teacher_Registration  

# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import TeacherForm
# from django.views.generic import ListView, DetailView

 
# def teacher_registration(request):
#     return render(request,"teacher_registration.html") 
 
# def insert(request):
#         if request.method == 'POST':
#             if request.POST.get('name',''):
#                 name= request.POST.get('name','')
#                 email= request.POST.get('email','')
#                 designation= request.POST.get('designation','')
#                 profile_photo= request.POST.get('profile_photo','')
#                 password= request.POST.get('password','')
#                 about= request.POST.get('about','')
#                 work_exp= request.POST.get('work_exp','')
#                 x=Teacher_Registration(name=name,email=email,designation=designation,profile_photo=profile_photo,password=password,about=about,work_exp=work_exp)
#                 x.save()
#                 print("DONE")
#             else:
#                 print("EMPTY")


             
                
#             return render(request,"teacher_registration.html") 

#         else:
#             print("ERROR")
#     