from django.urls import path
from .views import index, signup, login, logout, settings, upload, like_post, profile, search, follow, notifications, delete_notification, copy_to_clipboard, delete_post 

urlpatterns = [
    path('', index, name='index'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('follow', follow, name='follow'),
    path('search', search, name='search'),
    path('notifications', notifications, name='notifications'),
    path('delete_notification/<int:notification_id>', delete_notification, name='delete_notification'),
    path('share/<str:data>', copy_to_clipboard, name='copy_to_clipboard'),
    # path('question/edit/<int:question_id>/', edit_question, name='edit_question'),
    # path('answer/edit/<int:answer_id>/', edit_answer, name='edit_answer'),
    path('delete/<str:post_id>/', delete_post, name='delete_post'),
    path('profile/<str:pk>', profile, name='profile'),
    path('like-post', like_post, name='like-post'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]