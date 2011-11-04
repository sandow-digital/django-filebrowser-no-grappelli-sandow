from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    
    # filebrowser urls
    url(r'^browse/$', redirect_to, {'url': '/admin/business/photo/?_popup=1', 'permanent': True}, name="fb_browse"),
    url(r'^mkdir/', 'filebrowser.views.mkdir', name="fb_mkdir"),
    url(r'^upload/', 'filebrowser.views.upload', name="fb_upload"),
    url(r'^rename/$', 'filebrowser.views.rename', name="fb_rename"),
    url(r'^delete/$', 'filebrowser.views.delete', name="fb_delete"),
    url(r'^versions/$', 'filebrowser.views.versions', name="fb_versions"),
    
    url(r'^check_file/$', 'filebrowser.views._check_file', name="fb_check"),
    url(r'^upload_file/$', 'filebrowser.views._upload_file', name="fb_do_upload"),
    
)
