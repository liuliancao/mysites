from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'account/register.html') 



def login(request):
    return render(request,'account/login.html') 


def checklogin(request):
    pass

def logout(request):
    pass