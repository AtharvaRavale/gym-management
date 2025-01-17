from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns= [
    path('register/',views.Register.as_view(),name= 'register'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.logout_user,name='logout'),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('profile/', views.my_profile, name='my_profile'),

 ]