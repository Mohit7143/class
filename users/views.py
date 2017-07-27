from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginUser,RegisterUser
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate,login,logout

class UserLogin(View):
    form_class = LoginUser

    def get(self,request):
        return redirect('users:test')

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('drinks:index')
        return redirect('users:test')

class UserRegister(View):
    form_class = RegisterUser

    def get(self,request):
        return redirect('users:test')

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('drinks:index')

        return redirect('users:test')

def LogoutView(request):
    logout(request)
    return redirect('users:test') 

def test(request):
    log_form = LoginUser
    Reg_form = RegisterUser
    template = 'users/login_test.html'
    if request.user.is_authenticated:
            return redirect('drinks:index')
    context = {
     'form' : log_form,
     'tmp' : Reg_form,
    }
    return render(request , template ,context)