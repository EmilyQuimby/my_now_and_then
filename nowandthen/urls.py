from django.urls import path
from nowandthen import views

app_name = 'nowandthen'

urlpatterns = [
    path('', views.index, name='index'),
]
