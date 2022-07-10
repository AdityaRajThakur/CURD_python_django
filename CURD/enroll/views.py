from asyncio import exceptions
from django.shortcuts import render ,HttpResponseRedirect
from enroll.forms import StduentRegistration
from .models import User
from django.views.generic import CreateView
from django.http import Http404
 
# Create your views here.

class AddStudent(CreateView):
    model = User 
    form_class = StduentRegistration
    template_name = 'enroll/addandshow.html'
    success_url = '/login/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context 


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

