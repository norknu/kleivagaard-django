from django.shortcuts import render
from .models import NewsArticle

# Create your views here.

def frontpage_view(request):
    articles = NewsArticle.objects.all()
    return render(request, 'home.html', {
        'articles': articles
    })
