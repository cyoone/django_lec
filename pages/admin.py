from django.contrib import admin
from .models import Slides, Good, Post, New, Best, Comment
# 관리자 페이지에서 조작

class SlidesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['title']

class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'image']
    search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author__username']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']

admin.site.register(Slides, SlidesAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(New)
admin.site.register(Best)