from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage),
    path('about/', views.about),
    path('product/', views.product),
    path('product/<int:good_id>', views.detail, name='detail'),
    path('comment/create/<int:good_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('contact/', views.contact),
    path('contact/<int:post_id>', views.notice, name='notice'),
]