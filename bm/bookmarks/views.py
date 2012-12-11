from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.forms import ModelForm
from django.views.generic import ListView
from braces.views import LoginRequiredMixin
from bm.bookmarks.models import Bookmark


@login_required
def save_bookmark(request):
    if request.method == 'GET':
        form = BookmarkForm()
    else:
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            
    return render(request, "bookmarks/save_bookmark.html", {'form': form})

class BookmarkListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by('-create_date')

class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('user',)