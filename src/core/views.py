from django.shortcuts import render
from core.models import Post


def index(request):
    posts = Post.objects.all().order_by("-date_created")
    context = {
        "posts": posts,
    }
    return render(request, "index.html", context)
