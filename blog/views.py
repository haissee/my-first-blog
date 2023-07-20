from django.shortcuts import render
from django.utils import timezone
from .models import Post


def django_countries(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/django_countries.html', {'posts': posts})
