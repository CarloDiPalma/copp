from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'news/index.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'news/post_detail.html', context)
