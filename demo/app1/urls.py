from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("signup/",views.sign_up,name="signup"),
    path("",views.sign_in,name='login'),
    path("home/",views.home,name="home"),
    # path("changepass/",views.changepass,name="newpass")
    path('changepass/',views.changepass.as_view(),name="newpass"),
    path('forgetpass/',views.forgetpassword,name='forgetpass'),
    path("reset/<int:pk>", views.reset, name = "Resset"),
    path('password_change/done/',views.changepassdone.as_view(), name='password_change_done'),
 
    
    # path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    # path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    # path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')
]  

