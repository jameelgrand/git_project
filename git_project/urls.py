from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'git_project.views.home', name='home'),
    url(r'^$', include('importings.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
