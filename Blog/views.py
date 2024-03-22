# from datetime import date
from django.shortcuts import render,get_object_or_404
from .models import Post
all_posts =[]

# Create your views here.


def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    return render(request, "Blog/index.html",{
        "posts":latest_posts
    })


def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request, "Blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request,slug):
    identified_post=get_object_or_404(Post,slug=slug)
    return render(request,"Blog/post-detail.html",{
                  "post":identified_post,
                  "post_tags":identified_post.caption.all()
            })