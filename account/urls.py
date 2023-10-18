from django.urls import path
from django.urls import re_path
from . import views
# from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView ,PasswordResetConfirmView,PasswordResetCompleteView

# from django.contrib.auth import views as views
from account.views import PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [
  
    path('signup/', views.register_user, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    #Management
    re_path(r'^chgpwd/$', views.changepwview, name='chgpwd'),

    #Default Django Reset
    # path('password-reset/', views.PasswordResetView.as_view(template_name='registration/password_reset.html', html_email_template_name='registration/password_reset_email.html'),name='password-reset'),
    # path('password_reset/done/',views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),

    # path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    # path('password-reset-complete/',views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

     #reset password
    # path('password_reset/',views.PasswordResetView.as_view(),name='password_reset'),
    #   path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password_reset/',
    views.PasswordResetView.as_view(),
    name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/done/',
    views.PasswordResetDoneView.as_view(),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
    views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
    path('reset/done/',
    views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete'),
    
    path("mail/", views.test_send_mail, name="mail"),
   
]