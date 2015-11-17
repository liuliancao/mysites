from django.conf.urls import url,include
from cuteblog import views

urlpatterns = [
    url(r'^$',views.index),
]

