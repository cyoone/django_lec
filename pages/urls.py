from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('about/', views.about),
    path('product/', views.product),
    path('contact/', views.contact),
    path('product/<int:good_id>', views.detail, name='detail'),
]