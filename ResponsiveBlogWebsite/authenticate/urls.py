from django.urls import path
from . import views

app_name = 'authenticate'

urlpatterns = [
    path('SignUp',views.signup,name='signup'),
    path('login',views.signin,name="signin"),
    path('creating_user/',views.creating_user,name="creating_user"),
]
