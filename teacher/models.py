from django.db import models

class Teacher_Registration(models.Model):

   name = models.CharField(max_length = 50,null=True)
   email = models.EmailField(max_length=20,null=True)
   designation = models.CharField(max_length = 50,null=True)
   profile_photo=models.ImageField(upload_to="teacher")
   password = models.CharField(max_length = 50,null=True)
   about = models.CharField(max_length = 1000,null=True )
   work_exp = models.CharField(max_length = 50,null=True)
   selection =models.BooleanField(null=True)

   def __str__(self):
        return self.name + "-Selection Status= " + str(self.selection)

