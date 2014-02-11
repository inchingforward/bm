from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from bm.bookmarks.views import UserBookmarkListView, UserBookmarkDetailView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bm.views.index', name='index'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^bookmarks/', include('bm.bookmarks.urls')),
    url(r'^news/', include('bm.news.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    # Default to showing a user's bookmarks
    url(r'^(\w+)/$', UserBookmarkListView.as_view(), name='user_bookmarks'),
    url(r'^(\w+)/bookmarks/$', UserBookmarkListView.as_view(), name='user_bookmarks'),
    url(r'^(?P<username>\w+)/bookmarks/(?P<pk>\d+)/$', UserBookmarkDetailView.as_view(), name='user_bookmark_detail'), 
)
