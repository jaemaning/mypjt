from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    
    articles = Article.objects.all()
    
    context = {
        'articles' : articles
    }
    
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }
    
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')