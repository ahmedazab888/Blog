from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import PostForm


def all_posts(requst):
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts,
    }
    return render(requst, 'all_posts.html', context)


def post(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'details.html', context, id)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'create_post.html', context)


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }
    return render(request, 'edit_post.html', context)