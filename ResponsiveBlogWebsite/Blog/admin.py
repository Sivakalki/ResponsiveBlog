from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import blogs,user,comments

admin.site.register(blogs)
admin.site.register(user)
admin.site.register(comments)
