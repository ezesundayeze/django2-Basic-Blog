from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/<slug:slug>', views.about, name='about'),
    path('login/',  views.login, name='login'),
]