from django.conf.urls import url,include
from . import views

app_name = 'drinks'

urlpatterns = [
   url(r'^$',views.IndexView.as_view(),name="index"),
   url(r'^add/$',views.AddPost.as_view(), name="add"),
   url(r'^post/(?P<id>[0-9]+)/$', views.DetailsPost, name="details"),
   url(r'^addcomment/(?P<all>[-\w]+)/$',views.addcomment,name="addcomment")
]