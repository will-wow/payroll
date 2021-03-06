from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import timecard.urls

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(timecard.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
         (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
