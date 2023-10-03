from django.shortcuts import render
from .models import Slides, Good


def mainpage(request):
    slides_list = Slides.objects.all()
    good_list = Good.objects.all()
    return render(request, 'pages/mainpage.html', {'slides_list':slides_list})
def company(request):
    return render(request, 'pages/company_info.html')
def about(request):
    return render(request, 'pages/brand_about.html')
def product(request):
    return render(request, 'pages/product.html')
def contact(request):
    return render(request, 'pages/contact.html')