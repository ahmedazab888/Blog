from django.contrib import admin
from .models import Post, User

class PostAdminList(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_date')


admin.site.register(Post, PostAdminList)