from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from account.models import User
from cuteblog.models import Article
from django import forms
# Create your views here.



def get_articles(num=5,category='tec'):
    article_list_num = Article.objects.get(category=category).order_by('-date')[:num]
    return article_list_num

# search articles by category
def search_articles_by_category(category,username):
    user = User.objects.get(username=username)
    article_list_all = user.article_set.all()
    article_list = [ article for article in article_list_all if article.category == category ]
    return article_list
def user_index(request,username):
    username_self = request.session.get('username','friend')
    user = {}
    if username == 'friend':
        return HttpResponseRedirect('/account/login') 
    else:
        if username_self == username:
            write_access = True
        else:
            write_access = False
        user = User.objects.get(username=username)
        article_list_left = user.article_set.all()[:5]
        article_list_tec = search_articles_by_category('tec',username) 
        return render_to_response('cuteblog/user/index.html',{'user':user,'article_list_left':article_list_left,'article_list_tec':article_list_tec,'write_access':write_access,})

#不同的栏目
def aboutme(request,username):
    user = User.objects.get(username__exact=username)
    return render_to_response('cuteblog/user/aboutme.html',{'user':user,})
    '''
def shuo(request,username):
    user = User.objects.get(username__exact=username)
    shuo_list = user.shuo_set.all() 
    return render_to_response('cuteblog/user/shuo.html',{'shuo_list':shuo_list,}
#def show_lanmu(request,username,lanmu):
#    user = User.objects.get(username__exact=username) 
#    return render_to_response('cuteblog/user/'+lanmu+'.html',{'lanmu':user.lanmu,})
'''
def blog_index(request):
    return render_to_response('cuteblog/index.html')
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


