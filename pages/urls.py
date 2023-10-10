from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('about/', views.about),
    path('product/', views.product),
    path('product/<int:good_id>', views.detail, name='detail'),
    path('contact/', views.contact),
    path('contact/<int:post_id>', views.notice, name='notice'),
]