from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from social_book.models import Profile, Post, LikePost
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def settings(request,*args,**kwargs):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        if request.FILES.get('image')==None:
            image = user_profile.profileimg
            bio= request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg=image
            user_profile.bio=bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image')!=None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('social_book:settings')

    return render(request, 'social_book/setting.html', {'user_profile': user_profile})


def index(request, *args, **kwargs):
    user_object = User.objects.get(username=request.user.username)
    user_profile=Profile.objects.filter(user=user_object).first()
    posts=Post.objects.all()
    return render(request, 'social_book/index.html',{'user_profile': user_profile, 'posts':posts})


def upload(request, *args, **kwargs):
    if request.method == 'POST':
        user=request.user.username
        image=request.FILES.get('image_upload')
        caption = request.POST['caption']
        new_post=Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('social_book/index.html')
    else:
        return redirect('social/index.html')
def like_post(request,*args,**kwargs):
    username=request.user.username
    post_id=request.GET.get('post_id')
    post=Post.objects.get(id=post_id)
    like_filter=LikePost.objects.filter(post_id=post_id, username=username).first()
    if like_filter==None:
        new_like=LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes=post.no_of_likes+1
        post.save()
        return redirect('social_book:index')
    elif like_filter != None:
        like_filter.delete()
        post.no_of_likes=post.no_of_likes-1
        post.save()
        return redirect('social_book:index')
def profile(request, pk, *args, **kwargs):
    user_object=User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
    }
    return render(request, 'social_book/profile.html', context)




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
                #log user and redirect to settings.py
                user_login=auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('social_book:settings')


    else:
        messages.info(request, 'password not matching')
        return render(request, 'social_book/signup.html')
def signin(request, *args, **kwargs):
     if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('social_book:index')
        else:
            messages.info('credential invalid')
            return redirect('social_book:signin')
     else:
         return render(request,'social_book/signin.html')
def logout(request, *args, **kwargs):
     auth.logout(request)
     return redirect('social_book:signin')



