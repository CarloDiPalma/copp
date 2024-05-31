from django.shortcuts import render
from .models import Post, PostImage


def index(request):
    posts = Post.objects.filter(is_published=True)

    context = {'posts': posts}
    return render(request, 'news/index.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    images = PostImage.objects.filter(post=post)
    print(images)
    context = {'post': post, 'images': images}
    return render(request, 'news/post_detail.html', context)
