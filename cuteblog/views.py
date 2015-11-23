from django.shortcuts import render_to_response
from django.http import HttpResponse
from account.models import User
from cuteblog.models import Article
# Create your views here.



def get_articles(num):
    article_list_num = Article.objects.order_by('-date')[:num]
    return article_list_num
    
def index(request):
    username = request.session.get('username','friend')
    user = {}
    if username != 'friend':
        user = User.objects.get(username=username)
    article_list_10 = get_articles(10)
    return render_to_response('cuteblog/index.html',{'user':user,'article_list_10':article_list_10,'username':username,})

def article(request,username):
    user = User.objects.get(username__exact=username)
    article = Article.objects.get(user=user)
    article_list = user.article_set.all()
    return render_to_response('cuteblog/user/index.html',{'article_list':article_list,'username':username,})


def blog_login(request):
    return render_to_response('cuteblog/login.html')

            
# display special article specified by id
def article_self(request,article_id):
    article = Article.objects.get(id__exact=article_id)
    return render_to_response("cuteblog/sample_article.html",{'article':article})
