from django.urls import path
from social_book.views import index, signup

app_name = 'social_book'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
]
