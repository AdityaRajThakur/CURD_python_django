"""CURD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from enroll.views import AddStudent,UpdateStudent,DeleteStudent

app_name = 'CURD'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',AddStudent.as_view(),name = 'classviewaddstudent'),
    path('delete/<int:pk>' ,DeleteStudent.as_view() , name = 'delete_data'),
    path('update/<int:pk>/' ,UpdateStudent.as_view(), name = 'updatestudent'),
    path('login/',include('enroll.urls'), name = 'mylogin')
]
