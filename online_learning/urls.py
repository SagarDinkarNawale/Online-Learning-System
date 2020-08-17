from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('admin/', admin.site.urls),
   	path('', views.index,name='index'),
    path('teacher_registration', views.teacher_registration,name='teacher_registration'),
    path('insert', views.insert,name='insert'),
    path('upload_course', views.upload_course,name='upload_course'),

    path('courses', views.courses,name='courses'),
    path('news', views.news,name='news'),
    path('elements',views.elements,name='elements'),
    path('contact', views.contact,name='contact'),
    path('new_course', views.new_course,name='new_course'),
    path('message', views.message,name='message'),
    path('teacher_details', views.teacher_details,name='teacher_details'),


]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#  