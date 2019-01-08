from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.event_brief, name='event_brief'),
    url(r'^prov/$', views.event_list, name='event_list'),
    url(r'^event/(?P<pk>\d+)$', views.event_detail, name='event_detail'),
    url(r'^export/$', views.event_details_list, name='event_details_list'),
    url(r'^regulars/$', views.regulars_list, name='regulars_list'),
    url(r'^edit/(?P<pk>\d+)$', views.event_edit, name='event_edit'),
    url(r'^del/(?P<pk>\d+)$', views.event_delete, name='event_delete'),
]
