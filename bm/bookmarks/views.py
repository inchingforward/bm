from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bm.bookmarks.models import Bookmark


@login_required
def index(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by('-create_date')
    return render(request, "bookmarks/bookmark_list.html", {'bookmarks': bookmarks})
