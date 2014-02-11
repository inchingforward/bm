from django.conf.urls import patterns, include, url
from bm.bookmarks.views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDetailView


urlpatterns = patterns('',
    url(r'^$', BookmarkListView.as_view(), name='bookmarks_index'),
    url(r'^add$', BookmarkCreateView.as_view(), name='bookmark_create'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetailView.as_view(), name='bookmark_detail'),
    url(r'^(?P<pk>\d+)/edit/$', BookmarkUpdateView.as_view(), name='bookmark_update'),
    url(r'^fetchtitle$', 'bm.bookmarks.views.fetch_url_title'),
)
