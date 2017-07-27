from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
import datetime

class Article(models.Model):
    content = RichTextField(default="")
    title = models.CharField(max_length=200,default="")
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.content

class Comment(models.Model):
    Art =  models.ForeignKey(Article,on_delete=models.CASCADE)
    content = RichTextField(default="")
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.content

