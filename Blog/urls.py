from django.urls import path
from . import views

urlpatterns = [
    path('Blog/',views.first_page,name="first_page"),
    path('SignUp/',views.SignUp,name="SignUp"),
    
]
