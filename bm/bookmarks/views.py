from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from braces.views import LoginRequiredMixin
from bm.bookmarks.forms import BookmarkForm
from bm.bookmarks.models import Bookmark


class BookmarkCreateView(LoginRequiredMixin, CreateView):
        model = Bookmark
        form_class = BookmarkForm
        success_url = '/bookmarks/'
        
        def form_valid(self, form):
            form.instance.user = self.request.user
            messages.success(self.request, "Bookmark added.")
            return super(BookmarkCreateView, self).form_valid(form)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
        model = Bookmark
        form_class = BookmarkForm
        success_url = '/bookmarks/'

class BookmarkListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by('-create_date')

