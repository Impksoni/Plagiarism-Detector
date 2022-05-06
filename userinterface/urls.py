from django.urls import path
from . import views

app_name = "fileApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('result/', views.send_file, name = 'result'),
]
