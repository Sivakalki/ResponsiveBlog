from django.db import models

# Create your models here.
from django.db import models

class user(models.Model):
    username = models.CharField(max_length=30,default=None)
    userid = models.CharField(max_length=20, primary_key=True)
    mail = models.EmailField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.userid
    
class blogs(models.Model):
    userid = models.ForeignKey(user, on_delete=models.CASCADE)
    blogname = models.CharField(max_length=50)
    blog = models.CharField(max_length=10000000)
    blognum = models.IntegerField()
    likes = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)
    def __str__(self):
        return self.userid
    
class comments(models.Model):
    userid = models.ForeignKey(user,on_delete=models.CASCADE)
    blognum = models.ForeignKey(blogs, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
# Create your models here.
