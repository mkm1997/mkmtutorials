from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404


from .models import usersignup

from django.views.generic import TemplateView
from .forms import signup,info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('MKMTUTE'))


def contactus(request):
    if request.method == "POST":
        form = info(data=request.POST)
        if form.is_valid():
            form.save()
    form = info(data=request.POST)
    return render(request,'temp/home.html',{'form':form})



#for the search bar
def your_view(request):

    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box',None)

        print(search_query)

        li = ["python", "java", "html", "css", "c++", "None",]
        print(search_query)
        if search_query.lower() in li:
            return render(request,'temp/course.html',{})
        else:
            return HttpResponse("<h4>You are giving wrong input or searching for wrong course please make a correct search like enter python for python course</h2>")


class MKMTUTE(TemplateView):

    template_name = 'temp/course.html'



class check(TemplateView):
    template_name = 'temp/index.html'



class home(TemplateView):
    template_name = 'temp/home.html'


class cplusplus(LoginRequiredMixin,TemplateView):
    template_name = 'temp/c++.html'

class java(LoginRequiredMixin,TemplateView):
    template_name = 'temp/java.html'

class javascript(LoginRequiredMixin,TemplateView):
    template_name = 'temp/javascript.html'

class python(LoginRequiredMixin,TemplateView):
    template_name = 'temp/python.html'


class about(TemplateView):
    template_name = 'temp/aboutus.html'


class compile(TemplateView):
    template_name = 'temp/compiler.html'



