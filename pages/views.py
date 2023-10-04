from django.shortcuts import render
from .models import Slides, Good, Post, New, Best


def mainpage(request):
    slides_list = Slides.objects.all()
    new_list = New.objects.all()
    best_list = Best.objects.all()
    return render(request, 'pages/mainpage.html', {'slides_list':slides_list, 'new_list':new_list, 'best_list':best_list})

def about(request):
    return render(request, 'pages/brand_about.html')

def product(request):
    good_list = Good.objects.all()
    return render(request, 'pages/product.html', {'good_list':good_list})

def contact(request):
    post_list = Post.objects.order_by('-pub_date')
    return render(request, 'pages/contact.html', {'post_list':post_list})

def company(request):
    return render(request, 'pages/company_info.html')