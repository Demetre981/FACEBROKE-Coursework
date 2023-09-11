from django.urls import path
from .views import edit_post, index, signup, login, logout, settings, upload, like_post, profile, search, follow, notifications, delete_notification, copy_to_clipboard, delete_post, render_favourites, add_to_favourites

urlpatterns = [
    path('', index, name='index'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('follow', follow, name='follow'),
    path('search', search, name='search'),
    path('notifications', notifications, name='notifications'),
    path('delete_notification/<int:notification_id>', delete_notification, name='delete_notification'),
    path('share/<str:data>', copy_to_clipboard, name='copy_to_clipboard'),
    path('edit/<str:post_id>/', edit_post, name='edit_post'),
    path('add_to_favourites/<str:post_id>/', add_to_favourites, name='add_to_favourites'),
    path('favourites', render_favourites, name='render_favourites'),
    path('delete/<str:post_id>/', delete_post, name='delete_post'),
    path('profile/<str:pk>', profile, name='profile'),
    path('like-post', like_post, name='like-post'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]