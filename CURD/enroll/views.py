from asyncio import exceptions
from django.shortcuts import render ,HttpResponseRedirect
from enroll.forms import StduentRegistration
from .models import User

from django.http import Http404
 
# Create your views here.

def add_show(request):
    obj =  StduentRegistration() 
    object_list = User.objects.all() 
    if request.method=='POST':
        obj = StduentRegistration(request.POST)
        if obj.is_valid():
            obj.save()
            obj = StduentRegistration()

    return render(request,'enroll/addandshow.html' ,{'object':obj , 'object_list':object_list})


def delete_data(request ,id):
    if request.method=='POST':
        obj = User.objects.get(pk = id) 
        obj.delete()
        return HttpResponseRedirect('/')


def update_data(request ,id):
    
    if request.method=='POST':
        c_obj = User.objects.get(pk = id)
        fm = StduentRegistration(request.POST , instance=c_obj)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')    
    else:
        try:
            c_obj = User.objects.get(pk = id) 
            fm = StduentRegistration(instance =c_obj) 
        except:
            raise Http404('The Account that you are trying to update is not found..')
    return render(request , 'enroll/updatestudent.html', {'object' :fm})

