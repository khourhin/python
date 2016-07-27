from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsPost
from .forms import NewsForm

# Create your views here.

def news_list(request):
    news = NewsPost.objects.order_by('date')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(NewsPost, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})

def news_edit(request, pk):
    news = get_object_or_404(NewsPost, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.published_date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/create_news.html', {'form': form})
