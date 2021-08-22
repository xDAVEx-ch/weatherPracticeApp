from django.urls import path
from . import views

urlpatterns = [
    #path('url', function to execute, url name)
    path('', views.index, name='index')
]