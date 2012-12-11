from django.conf.urls import patterns, include, url
from bm.bookmarks.views import BookmarkListView


urlpatterns = patterns('',
    url(r'^$', BookmarkListView.as_view(), name='bookmarks_index'),
    url(r'^save/', 'bm.bookmarks.views.save_bookmark', name='save_bookmark'),
)
