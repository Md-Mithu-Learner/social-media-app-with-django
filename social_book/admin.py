from django.contrib import admin
from social_book.models import User, Profile, Post, LikePost,FollowersCount

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio','profileimg',)
    search_fields = ('user',)
admin.site.register([Post,LikePost,FollowersCount])


