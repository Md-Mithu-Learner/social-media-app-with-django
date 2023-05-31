from django.urls import path
from social_book.views import index, signup, signin, logout, settings,upload, like_post,profile

app_name = 'social_book'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('settings/', settings, name='settings'),
    path('upload/', upload, name='upload'),
    path('like-post/',like_post, name='like_post'),
    path('profile/<str:pk>/', profile, name='profile'),
]
