from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from social_book.models import Profile
from django.contrib import messages


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'social_book/index.html', )

def signup(request, *args, **kwargs):
    data = request.POST
    if request.method == 'POST':
        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'username taken')
                return redirect('social_book:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('social_book:signup')
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('social_book:signup')


    else:
        messages.info(request, 'password not matching')
        return render(request, 'social_book/signup.html')
