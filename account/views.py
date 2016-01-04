from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from account.models import User

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField()
    headimg = forms.FileField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField()

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            headimg = uf.cleaned_data['headimg']
            errors = []
            if User.objects.filter(username__exact=username):
                errors.append('username exists.')
                return render_to_response('account/register.html',{'uf':uf,'errors':errors})
            else:
                User.objects.create(username=username,password=password,headimg=headimg)
                request.session['username']=username
                return HttpResponseRedirect('/blog/'+username)
    else:
        uf = UserForm()        
    return render_to_response('account/register.html',{'uf':uf},) 



def login(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if  uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            errors = []
            if User.objects.filter(username__exact=username,password__exact=password):
                request.session['username'] = username
                return HttpResponseRedirect('/blog/'+username)
            else:
                errors.append("username and password doesn't match")
                return render_to_response('account/login.html',{'uf':uf,'errors':errors})
        else:
            return HttpResponse('haha')
    else:
        uf = UserForm()
    return render_to_response('account/login.html',{'uf':uf})


def logout(request):
    try:
        del request.session['username']
    finally:
        return HttpResponseRedirect('/blog')
