from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Article
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .forms import initform,commentadd
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

class IndexView(LoginRequiredMixin,generic.ListView):
    login_url = 'users:login'

    def get(self,request):
        contact_list = Article.objects.all()
        paginator = Paginator(contact_list, 5)  # Show 5 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'drinks/index.html', {'form': contacts})


def DetailsPost(request,id):
    if request.user.is_authenticated:
        try:
            post = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            raise Http404("Post Does not Exist in our database")
        return render(request , 'drinks/details.html' ,{'all' : post}) 
    return redirect('users:login')       
        


class AddPost(LoginRequiredMixin,View):
    login_url = 'users:login'
    form_class = initform
    template = 'drinks/reg.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.admin = request.user
            post.save()

            return redirect('drinks:index')
        return render(request,self.template,{'form':form})     


def addcomment(request,all):
    if request.user.is_authenticated:
        form = commentadd(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.admin = request.user
            comment.Art = all
            comment.save()

            return redirect('drinks:index')
        else:
            return HttpResponse("No comment")
    return redirect('users:login')  