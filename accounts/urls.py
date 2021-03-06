from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashbaord'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPasswordLink/<uidb64>/<token>', views.resetPasswordLink, name='resetPasswordLink'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]
