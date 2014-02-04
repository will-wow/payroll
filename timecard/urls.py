from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', views.Days, name='timecard'),
)