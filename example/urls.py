from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^one/$', 'example.views.one'),
    (r'^two/$', 'example.views.two'),
)
