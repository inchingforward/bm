from django.shortcuts import render, redirect
from bm.bookmarks.views import BookmarkListView


def index(request):
    if request.user.is_authenticated():
        return redirect('bookmarks_index')
    
    return render(request, "index.html")