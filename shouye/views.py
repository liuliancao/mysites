from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    username = request.session.get('username','friend')
    return render_to_response('index.html',{'username':username})
