from django.conf.urls import patterns, url

from people import views

urlpatterns = patterns('',
    # ex: /person/
    url(r'^$', views.index, name='index'),
    # ex: /person/5/
    url(r'^(?P<person_id>\d+)/$', views.person_detail, name='person_detail'),
    # ex: /person/5/quotes/
    url(r'^(?P<person_id>\d+)/quotes/$', views.person_quotes, name='results'),
    url(r'^(?P<person_id>\d+)/(?P<quote_id>\d+)/$', views.quote_detail, name='quote_detail'),
)
