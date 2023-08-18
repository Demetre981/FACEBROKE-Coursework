from django.urls import path
from .views import index, signup, login, logout, settings, upload, like_post

urlpatterns = [
    path('', index, name='index'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('like-post', like_post, name='like-post'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    
]