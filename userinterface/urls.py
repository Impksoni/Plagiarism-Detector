from django.urls import path
from . import views

app_name = "fileApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('result/', views.send_file, name = 'result'),
]
