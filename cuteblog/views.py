from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'cuteblog/index.html')

def blog(request):
    return render(request,'cuteblog/index.html')


def blog_login(request):
    return render(request,'cuteblog/login.html')

#def checklogin(request):
            
