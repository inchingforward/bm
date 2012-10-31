from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'bm.bookmarks.views.index', name='bookmarks'),
)
