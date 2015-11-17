from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register',views.register),
    url(r'login',views.login),
    url(r'checklogin','django.contrib.auth.views.login',{'template_name':'account/login.html'}),
    url(r'logout/',views.logout),
]
