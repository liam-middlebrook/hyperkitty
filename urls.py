from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from api import EmailResource, ThreadResource, SearchResource

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hyperkitty.views.home', name='home'),
    # url(r'^hyperkitty/', include('hyperkitty.foo.urls')),
    # This will be the new index page
    url(r'^$', 'views.pages.index'),
    url(r'^/$', 'views.pages.index'),
    # This will be the new archives page
    url(r'^archives/(?P<mlist_fqdn>.*@.*)/(?P<year>\d{4})/(?P<month>\d\d?)/$', 'views.pages.archives'),
    url(r'^archives/(?P<mlist_fqdn>.*@.*)/(?P<year>\d{4})/(?P<month>\d\d?)$', 'views.pages.archives'),
    url(r'^archives/(?P<mlist_fqdn>.*@.*)/$', 'views.pages.archives'),
    url(r'^archives/(?P<mlist_fqdn>.*@.*)$', 'views.pages.archives'),
    # The thread view
    url(r'^thread/(?P<mlist_fqdn>.*@.*)/(?P<threadid>.+)$', 'views.pages.thread'),
    # This will be the new recent page
    url(r'^list$', 'views.pages.index'),
    url(r'^list/$', 'views.pages.index'),
    url(r'^list/(?P<mlist_fqdn>.*@.*)/$', 'views.pages.list'),
    url(r'^list/(?P<mlist_fqdn>.*@.*)$', 'views.pages.list'),
    # Single message view
    url(r'^message/(?P<mlist_fqdn>.*@.*)/(?P<messageid>.+)$', 'views.pages.message'),
    # Search
    #url(r'^search$', 'views.pages.search'),
    # If page number is present in URL
    url(r'^search/(?P<mlist_fqdn>.*@.*)\/(?P<target>.*)\/(?P<keyword>.*)\/(?P<page>\d+)/$', 'views.pages.search_keyword'),
    url(r'^search/(?P<mlist_fqdn>.*@.*)\/(?P<target>.*)\/(?P<keyword>.*)\/(?P<page>\d+)$', 'views.pages.search_keyword'),
    # Show the first page as default when no page number is present in URL
    url(r'^search/(?P<mlist_fqdn>.*@.*)\/(?P<target>.*)\/(?P<keyword>.*)/$', 'views.pages.search_keyword'),
    url(r'^search/(?P<mlist_fqdn>.*@.*)\/(?P<target>.*)\/(?P<keyword>.*)$', 'views.pages.search_keyword'),
    
    url(r'^search/(?P<mlist_fqdn>.*@.*)/$', 'views.pages.search'),
    url(r'^search/(?P<mlist_fqdn>.*@.*)$', 'views.pages.search'),
    url(r'^tag/(?P<mlist_fqdn>.*@.*)\/(?P<tag>.*)$', 'views.pages.search_tag'),
    # mockups:
    url(r'^mockup/$', 'views.mockup.index'),
    url(r'^mockup/archives$', 'views.mockup.archives'),
    url(r'^mockup/archives/(?P<year>\d{4})/(?P<month>\d{2})/$', 'views.mockup.archives'),
    url(r'^mockup/recent$', 'views.mockup.recent'),
    url(r'^mockup/search$', 'views.mockup.search'),
    url(r'^mockup/search\/(?P<keyword>.*)$', 'views.mockup.search_keyword'),
    url(r'^mockup/tag\/(?P<tag>.*)$', 'views.mockup.search_tag'),

    # REST API
    url(r'^api/$', 'views.pages.api'),
    url(r'^api/email\/(?P<mlist_fqdn>.*@.*)\/(?P<messageid>.*)/',  EmailResource.as_view()),
    url(r'^api/thread\/(?P<mlist_fqdn>.*@.*)\/(?P<threadid>.*)/',  ThreadResource.as_view()),
    url(r'^api/search\/(?P<mlist_fqdn>.*@.*)\/(?P<field>.*)\/(?P<keyword>.*)/',  SearchResource.as_view()),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
#) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

