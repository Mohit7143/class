from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginUser,RegisterUser
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate,login,logout

class UserLogin(View):
    form_class = LoginUser
    template = 'users/login.html'

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('drinks:index')
        form = self.form_class(None)
        return render(request , self.template ,{'form': form})

    def post(self,request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('drinks:index')
        return render(request, 'users/login.html', {'form': form})

class UserRegister(View):
    form_class = RegisterUser
    template = 'users/register.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

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

        return render(request, self.template, {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('users:login') 

def test(request):
    return render(request,'users/login_test.html')  