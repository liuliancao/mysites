from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from account.models import User
from cuteblog.models import Article
from django import forms
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
    article_list = []
    try:
        user = User.objects.get(username__exact=username)
    except:
        pass
    else:
        article_list = user.article_set.all()
    finally:
        return render_to_response('cuteblog/user/index.html',{'article_list':article_list,'username':username,})


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
