from django.shortcuts import render, redirect
from bm.news.models import NewsItem


def index(request):
    if request.user.is_authenticated():
        return redirect('bookmarks_index')
    
    news = NewsItem.objects.all().order_by('-create_date')[0:5]
    
    return render(request, 'index.html', {'news': news})