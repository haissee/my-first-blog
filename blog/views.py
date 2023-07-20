from django.shortcuts import render

# Create your views here.
def django_countries(request):
    return render(request, 'blog/django_countries.html', {})