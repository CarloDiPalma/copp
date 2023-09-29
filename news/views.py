from django.shortcuts import render
from .models import Post


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'news/post_detail.html', context)
