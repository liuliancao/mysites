from django.conf.urls import url,include
from cuteblog import views
from account import views as account_views

urlpatterns = [
    url(r'^$',views.index),
    url(r'(.*)/(?P<article_id>(\d+))$',views.article_self),
    url(r'^(?P<username>([^/]+))/$',views.user_index),
    url(r'(?P<username>([^/]+))/write_blog$',views.write_blog),
    url(r'(?P<username>([^/]+))/(?P<category>([^/]+))/$',views.search_articles_by_category),
    url(r'/write_blog$',account_views.login),
]



