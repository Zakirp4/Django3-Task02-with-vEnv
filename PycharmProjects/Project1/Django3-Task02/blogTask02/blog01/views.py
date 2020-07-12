from django.shortcuts import render
from .models import Post, Author

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html',{'authors':authors})

def authors_post (request,author_name):

    posts = Post.objects.filter(author=author_name)

    return render(request, 'blog/authors_post.html', {'posts': posts, 'name': author_name})



def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }

    return render(request,'blog/post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

def test(request):
    return render(request, 'blog/test2.html')

