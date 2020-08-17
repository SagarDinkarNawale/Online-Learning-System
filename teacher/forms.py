from django import forms
from .models import Teacher_Registration

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher_Registration
        fields = "__all__"