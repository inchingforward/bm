from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'bm.bookmarks.views.index', name='bookmarks_index'),
    url(r'^save/', 'bm.bookmarks.views.save_bookmark', name='save_bookmark'),
)
