from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    #↓27で書き換え
    path("login/", views.LoginView.as_view(), name="login"), 
    #↓27で追加
     path("friends/", views.friends, name="friends"),
    #↓28で追加
     path("settings/", views.settings, name="settings"),
]