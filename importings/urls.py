from django.conf.urls import patterns, url

from importings import views

urlpatterns = patterns('',
    #url(r'jaam/$', views.index, name='index'),
    #url(r'prvs/$', views.prvs, name='prvs'),
    #url(r'block/$', views.block, name='block'),
    #url(r'ajax/$', views.menu, name='menu'),
    url(r'^$', views.Home, name='home'),
    #url(r'ajax/contact$', views.contact, name='contact'),
    # ex: /polls/5/
    #url(r'^(?P<shirts_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/order/
    #url(r'^(?P<shirts_id>\d+)/order/$', views.order, name='order'),
   
)