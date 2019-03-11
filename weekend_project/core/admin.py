from django.contrib import admin

# Register your models here.

from core.models import Blog_Posts, Blog_User

admin.site.register(Blog_Posts)

admin.site.register(Blog_User)