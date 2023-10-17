from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Slides, Good, Post, New, Best, Comment
from .forms import CommentForm


def mainpage(request):
    slides_list = Slides.objects.all()
    good_list = Good.objects.all()
    new_list = New.objects.all()
    best_list = Best.objects.all()
    context = {'slides_list':slides_list, 'good_list':good_list, 'new_list':new_list, 'best_list':best_list}
    return render(request, 'pages/mainpage.html', context)

def about(request):
    return render(request, 'pages/brand_about.html')

def product(request):
    good_list = Good.objects.all()
    return render(request, 'pages/product.html', {'good_list':good_list})

def detail(request, good_id):
    good_list = get_object_or_404(Good, pk=good_id)
    context = {'good_list': good_list}
    return render(request, 'pages/product_detail.html', context)

@login_required(login_url='accounts:login')
def comment_create(request, good_id):
    good_list = get_object_or_404(Good, pk=good_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = good_list
            comment.author = request.user
            comment.save()
            return redirect('detail', good_id=good_list.id)
        else:
            form = CommentForm()
        context = {'good_list': good_list, 'form': form}
        return render(request, 'pages/product_detail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', good_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(request, 'pages/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied

    else:
        comment.delete()
    return redirect('detail', good_id=comment.content_list.id)

def contact(request):
    post_list = Post.objects.order_by('-pub_date')
    return render(request, 'pages/contact.html', {'post_list':post_list})

def notice(request, post_id):
    post_list = get_object_or_404(Post, pk=post_id)
    context = {'post_list': post_list}
    return render(request, 'pages/notice_detail.html', context)

def company(request):
    return render(request, 'pages/company_info.html')