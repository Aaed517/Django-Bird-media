from django.urls import path

from main import views
app_name = 'Main'

urlpatterns = [
        path('',views.index , name='index'),
]
