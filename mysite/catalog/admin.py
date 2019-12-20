from django.contrib import admin
from .models import Social, BlogPost, Member

admin.site.register(Social)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_socials')

