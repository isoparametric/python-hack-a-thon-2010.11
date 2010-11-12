
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'quest.views.index', name='quest_index'),
    url(r'^accept$', 'quest.views.accept', name='quest_accept'),
    url(r'^advance$', 'quest.views.advance', name='quest_advance'),
)
