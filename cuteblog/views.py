from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from account.models import User
from cuteblog.models import Article
from django import forms
# Create your views here.



def get_articles(num):
    article_list_num = Article.objects.order_by('-date')[:num]
    return article_list_num

# search articles by category
def search_articles_by_category(request,category,username):
    user = User.objects.get(username=username)
    article_list_all = user.article_set.all()
    if category == 'feedback':
        return render_to_response('cuteblog/feedback.html',{'user':user,})
    elif category == 'articles':
        return render_to_response('cuteblog/category.html',{'article_list':article_list_all,})
    else:  
        article_list = [ article for article in article_list_all if article.category== category ]
        return render_to_response('cuteblog/category.html',{'article_list':article_list,})
def index(request):
    username = request.session.get('username','friend')
    user = {}
    if username != 'friend':
        user = User.objects.get(username=username)
    article_list_10 = get_articles(10)
    return render_to_response('cuteblog/index.html',{'user':user,'article_list_10':article_list_10,})

def user_index(request,username):
    article_list = []
    user={}
    write_access = False
    try:
        user = User.objects.get(username__exact=username)
    except:
        pass
    else:
        username_session = request.session['username']
        article_list = user.article_set.all()
        if username_session == username:
            write_access = True
    finally:
        return render_to_response('cuteblog/user/index.html',{'article_list':article_list,'user':user,'write_access':write_access,})


def blog_login(request):
    return render_to_response('account/login.html')

            
# display special article specified by id
def article_self(request,article_id):
    article = Article.objects.get(id__exact=article_id)
    return render_to_response("cuteblog/sample_article.html",{'article':article})


# for writing blogs.
class Write_blogform(forms.Form):
    title = forms.CharField(max_length=20)
    text = forms.CharField(widget=forms.Textarea)

def write_blog(request,username):
    try:
        username_session = request.session['username']
    except:
        return HttpResponseRedirect("/account/login")
    else:
        if request.method == 'POST':
            uf = Write_blogform(request.POST)    
            if uf.is_valid():
                title = uf.cleaned_data['title']
                text = uf.cleaned_data['text']
                username = request.session['username']
                try:
                    user = User.objects.get(username__exact=username)
                except:
                    return render_to_response("cuteblog/login.html")
                else:
                    Article.objects.create(title=title,text=text,user=user)
                finally:
                    return HttpResponseRedirect('/blog/liuliancao/')
              
        else:
             uf = Write_blogform()
        return render_to_response("cuteblog/user/write_blog.html",{'Write_blogform':uf,'username':username})


