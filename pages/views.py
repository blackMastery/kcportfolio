from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import render
from .forms import ProjectForm
from .models import Intros
from django.core.mail import send_mail

# Create your views here.




class Index(View):
    intro = None
    template_name = 'pages/index.html'

    def get(self, request):
        self.intro =  Intros.objects.filter(status='published')
        return render(request, self.template_name, {"intro": self.intro[0].statement})





class Contact(View):
    template_name = 'pages/contact/contact.html'
    projectform = ProjectForm()

    def get(self, request):
        return render(request, self.template_name, {'projectform': self.projectform})


    def post(self, request):

        form = ProjectForm(request.POST) 
        if form.is_valid():
            cd =  form.cleaned_data
            form.save()
            subject  = cd['title']
            budget =  cd['budget']
            description =  cd['description']
            thanks_mesage =  "Thank you, I'm looking forward to working with you"


            message = "budget: {} Description: {}".format(budget, description)

            send_mail(subject, message,'black.king1232@gmail.com', recipient_list=['black.king1232@gmail.com', 'kev.cadogan300@gmail.com'], fail_silently=False)
            return render(request, self.template_name, {'projectform': self.projectform,
             'thanks': thanks_mesage})



    



class Projects(View):
    template_name = 'pages/projects/project.html'

    def get(self, request):
        return render(request, self.template_name)




class Services(View):
    template_name = 'pages/services/service.html'

    def get(self, request):
        return render(request, self.template_name) 