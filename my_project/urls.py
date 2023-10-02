"""
가장 상위 URL 매핑 파일
"""
from django.contrib import admin
from django.urls import path, include
#from mysite import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mysite/", include('mysite.urls')),
    path('', include('pages.urls')),
]
