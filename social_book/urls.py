from django.urls import path
from social_book.views import index, signup, signin, logout, settings

app_name = 'social_book'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('settings/', settings, name='settings')
]
