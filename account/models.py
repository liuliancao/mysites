from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    headimg = models.FileField(upload_to='./static/upload')
    background = models.FileField(upload_to='./static/upload',default='./static/upload/bbb.jpg')
    signature = models.CharField(max_length=30,default='交个朋友吧')
    level = models.CharField(max_length=5,default='1')
    register_time = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.username + self.signature
