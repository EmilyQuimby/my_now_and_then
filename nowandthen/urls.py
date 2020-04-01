from django.urls import path
from nowandthen import views

app_name = 'nowandthen'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_picture/', views.add_picture, name='add_picture'),
    path('add_comment/<int:p.image_id>', views.add_comment, name='add_comment'),
    path('photo_feed/', views.photo_feed, name='photo_feed'),
    path('1970/', views.photo70, name='1970'),
    path('1980/', views.photo80, name='1980'),
    path('2010/', views.photo10, name='2010'),
    path('search/', views.search_results, name='search_results'),
]
