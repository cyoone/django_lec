from django.contrib import admin
from .models import Slides, Good, Post, New, Best
# 관리자 페이지에서 조작
admin.site.register(Slides)
admin.site.register(Good)
admin.site.register(Post)
admin.site.register(New)
admin.site.register(Best)