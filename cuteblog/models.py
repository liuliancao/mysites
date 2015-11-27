from django.db import models
from account.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    category = models.TextField(max_length=30,null=True)
    def __str__(self):
        return self.title 
        
