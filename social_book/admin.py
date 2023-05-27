from django.contrib import admin
from social_book.models import User, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio','profileimg',)
    search_fields = ('user',)



