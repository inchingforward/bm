from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bm.bookmarks.views.index', name='index'),
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^bookmarks/', include('bm.bookmarks.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
