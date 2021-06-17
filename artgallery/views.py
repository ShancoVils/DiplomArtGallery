from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views import generic
from .forms import  RegisterUserForm, LoginUserForm, AddWorkForm, AddRequestForm,ChangeLoginForm, ImageForm
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.views.generic.edit import CreateView , UpdateView
from django.contrib import auth
from django.views.generic import TemplateView
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from .models import Works, CustomUser, Request
from django.db.models import Count, fields
from django.contrib.auth import authenticate, login

from artgallery import forms






#Загрузка шаблона авторзиации


    
#Загрузка главной страницы


def main(request):
    template = loader.get_template('main/index.html')
    extra_context = {'Works': Works.objects.all().order_by('-id'), 'CustomUser': CustomUser.objects.all()}
    context =  {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)


def CategoryIllustrator(request):
    template = loader.get_template('categories/CategoryIllustrator.html')
    extra_context = {'Works': Works.objects.filter(category='Illustrator art').order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)

def CategoryLanding(request):
    template = loader.get_template('categories/CategoryLanding.html')
    extra_context = {'Works': Works.objects.filter(category='Landing page').order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)

def CategoryPhoto(request):
    template = loader.get_template('categories/CategoryPhoto.html')
    extra_context = {'Works': Works.objects.filter(category='Photo').order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)


def CategoryPhotoshop(request):
    template = loader.get_template('categories/CategoryPhotoshop.html')
    extra_context = {'Works': Works.objects.filter(category='Photoshop art').order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)


def CategoryProduct(request):
    template = loader.get_template('categories/CategoryProduct.html')
    extra_context = {'Works': Works.objects.filter(category='Product design').order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)
   

def CategoryUI(request):
    template = loader.get_template('categories/CategoryUI.html')
    extra_context = {'Works': Works.objects.filter(category='UI').order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)





def testcrud(request):
    template = loader.get_template('addwork/addwork.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def AutorsPage(request):
    template = loader.get_template('autors/autors.html')
    extra_context = {'CustomUser': CustomUser.objects.all(), 
    'Works': Works.objects.all().values('autor_id').annotate(total=Count('autor_id')).order_by('total')}
    #extra_context = {'CustomUser': CustomUser.objects.all(), 'Works': Works.objects.annotate(count_autor=Count('autor_id'))}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)

    




class LoginUser( LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

 



def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
        else:
            form = RegisterUserForm()


    return render(request, 'registration/login.html', {'form': form})





def logout_user(request):
    logout(request)
    return redirect('main')


def login_or_reg(request):
    if 'password2' in request.POST:
        return register(request)
    return LoginUser.as_view()(request)




def ProfileLike(request):
    template = loader.get_template('profiles/index.html')
    extra_context = {'Works': request.user.work_one.all().order_by('-id')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)



def Work_category(request):
    template = loader.get_template('work_category/index.html')
    extra_context = {'Works': Works.objects.all(), 'CustomUser': CustomUser.objects.all()}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)


class WorkCreate(CreateView):
    model = Works
    form_class = AddWorkForm
    extra_context = {'Works': Works.objects.all()}
    template_name = 'addwork/addwork.html'
    success_url = reverse_lazy('main')


class Contacts(CreateView):
    model = Request
    form_class = AddRequestForm
    extra_context = {'Request': Request.objects.all()}
    template_name = 'contacts/index.html'
    success_url = reverse_lazy('main')


def Workpage(request, works_id):
    template = loader.get_template('workpage/index.html')
    stuff = get_object_or_404(Works, id = works_id)
    liked=False
    if stuff.like.filter(id = request.user.id).exists():
        liked = True

    extra_context = {'Works': Works.objects.filter(id= works_id ), 'CustomUser': CustomUser.objects.all()
    }
    extra_context["liked"] = liked
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)
    


def Autorpage(request, customuser_id):
    template = loader.get_template('anotherprofiles/index.html')
    extra_context = {
    'CustomUser': CustomUser.objects.filter(id= customuser_id ),
    'Works': Works.objects.filter(autor_id= customuser_id ),  
    'WorksCount': Works.objects.values('autor_id').annotate(total=Count('autor_id')).order_by('total'),
    'LikeCount': Works.objects.values('likes').annotate(likesgs=Count('likes')).order_by('likesgs')}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)



def Profile_option(request):
    template = loader.get_template('profile_option/index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)




class LoginUserChange(UpdateView): 
    model = CustomUser
    template_name = 'profile_option/index.html'
    fields = ['name', 'email', 'bill_number', 'background_image']
    success_url = reverse_lazy('main')


 

class PasswordUserChang( CreateView):
     form_class = RegisterUserForm
     template_name = 'profile_option/index.html'
     success_url = reverse_lazy('main')
 

def options_profile(request):
    if 'password2' in request.POST:
        return PasswordUserChang.as_view()(request)  
    return LoginUserChange.as_view()(request)



class Contacts(CreateView):
    model = Request
    form_class = AddRequestForm
    extra_context = {'Request': Request.objects.all()}
    template_name = 'contacts/index.html'
    success_url = reverse_lazy('main')
    


def LikeView(request, pk):
    work = get_object_or_404(Works, id = request.POST.get('work_id'))
    liked = False
    if work.like.filter(id = request.user.id).exists():
        work.like.remove(request.user)
        liked = False
    else: 
        work.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('workpage', args=[str(pk)]))
    

def Popular(request):
    template = loader.get_template('popular_works/index.html')
    extra_context = {'Works': Works.objects.annotate(like_count=Count('like')).order_by('-like_count'),
     'CustomUser': CustomUser.objects.all()}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)


def Addavatar(request, pk):
    if request.method == 'POST':
        AvatarChandge(request, pk)
    else:
        template = loader.get_template('profiles/index.html')
        extra_context = {'Works': Works.objects.filter(autor=request.user).order_by('-id'),
        'Like': request.user.work_one.all()}
        context = {}
        rendered_page = template.render(extra_context, request)
        return HttpResponse(rendered_page)
    template = loader.get_template('profiles/index.html')
    extra_context = {'Works': Works.objects.filter(autor=request.user).order_by('-id'),
    'Like': request.user.work_one.all()}
    context = {}
    rendered_page = template.render(extra_context, request)
    return HttpResponse(rendered_page)


def AvatarChandge(request, pk):
    if request.POST:
        user_edit_form = ImageForm(request.POST,request.FILES, instance=request.user)
        if user_edit_form.is_valid():
            user_edit_form.save()