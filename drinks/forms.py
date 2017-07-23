from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Article,Comment


class initform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content',]


class commentadd(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content',]