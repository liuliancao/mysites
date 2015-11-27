from django.conf.urls import url,include
from cuteblog import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'(.*)/(?P<article_id>(\d+))$',views.article_self),
    url(r'^(?P<username>([^/]+))/$',views.article),
    url(r'(?P<username>([^/]+))/write_blog$',views.write_blog),
]



