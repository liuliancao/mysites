"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from shouye import views as shouye_views
from cuteblog import urls as cuteblog_urls
from account import urls as account_urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #首页
    url(r'^$',shouye_views.index),
    #blog
    url(r'^blog/', include(cuteblog_urls)),
    #用户有关
    url(r'^account/',include(account_urls)),
] + staticfiles_urlpatterns()