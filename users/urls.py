from django.conf.urls import url,include
from . import views

app_name = 'users'

urlpatterns = [
  url(r'^login/$', views.UserLogin.as_view(),name="login"),
  url(r'^logout/$', views.LogoutView,name="logout"),
  url(r'^register/$',views.UserRegister.as_view(),name="register"),
  url(r'^test/$',views.test,name="test"),
]