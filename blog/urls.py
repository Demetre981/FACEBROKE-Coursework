from django.urls import path
from .views import index, signup, login, logout, settings, upload, like_post, profile, search, follow 

urlpatterns = [
    path('', index, name='index'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('follow', follow, name='follow'),
    path('search', search, name='search'),
    path('profile/<str:pk>', profile, name='profile'),
    path('like-post', like_post, name='like-post'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]