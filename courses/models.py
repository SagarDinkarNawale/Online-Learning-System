from django.db import models

class course_registration(models.Model):

   cname = models.CharField(max_length = 50,null=True)
   cdiscription = models.CharField(max_length =30,null=True)
   cphoto=models.ImageField(upload_to="course")
   temail = models.EmailField(max_length=20,null=True)

   tpassword = models.CharField(max_length = 50,null=True)
   ccategory = models.CharField(max_length = 1000,null=True )
   cfile = models.FileField(upload_to='documents/')


   teacher_name = models.CharField(max_length = 50,null=True)
   teacher_designation = models.CharField(max_length = 50,null=True)
   teacher_profile_photo=models.ImageField(upload_to="teacher")
  

   def __str__(self):
        return str(self.cname)

class course_count(models.Model):
   web_dev = models.IntegerField()
   soft_dev = models.IntegerField()
   banking = models.IntegerField() 
   civil_services = models.IntegerField()
   social_media = models.IntegerField()
   
        


