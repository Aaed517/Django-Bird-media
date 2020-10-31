from django.urls import path

from account import views

app_name = 'Account'

urlpatterns = [
    path('register/',views.register , name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
