from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from braces.views import LoginRequiredMixin
from bm.bookmarks.forms import BookmarkForm
from bm.bookmarks.models import Bookmark
from BeautifulSoup import BeautifulSoup
import requests


def fetch_url_title(request):
    title = ''
    try:
        url = request.GET.get('url', '')
        if url:
            result = requests.get(url)
            if result and result.status_code == 200:
                soup = BeautifulSoup(result.content)
                if soup.title:
                    title = soup.title.string
    except Exception as e:
        print 'unexpected fetch_url_title error: %s' % e
    
    return HttpResponse(title)

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

class UserBookmarkListView(ListView):
    def get_context_data(self, **kwargs):
            context = super(ListView, self).get_context_data(**kwargs)
            context.update({
                'specified_user': self.args[0],
            })
            return context
    
    def get_queryset(self):
        user = get_object_or_404(User, username__iexact=self.args[0])
        return Bookmark.objects.filter(user=user).filter(private=False).order_by('-create_date')

