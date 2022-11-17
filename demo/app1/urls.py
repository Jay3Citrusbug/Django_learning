from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("signup/",views.sign_up,name="signup"),
    path("",views.sign_in,name='login'),
    path("home/",views.home,name="home")
]  

