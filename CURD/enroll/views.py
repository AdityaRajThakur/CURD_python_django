from enroll.forms import StudentRegistration
from .models import User
from django.views.generic import CreateView,DeleteView, UpdateView
 
# Create your views here.

class AddStudent(CreateView):
    model = User 
    form_class = StudentRegistration
    template_name = 'enroll/addandshow.html'
    success_url = '/login/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context 

class UpdateStudent(UpdateView):
    model = User 
    form_class  = StudentRegistration
    template_name = 'enroll/updatestudent.html' 
    success_url = '/login/'


class DeleteStudent(DeleteView):
    model = User 
    success_url = '/'
    template_name = 'enroll/DeleteStudent.html' 
