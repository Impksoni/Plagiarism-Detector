from django.urls import path
from . import views

app_name = "fileApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('upload/', views.send_file, name = 'upload'),
]
