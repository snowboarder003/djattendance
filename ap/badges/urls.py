from django.conf.urls import patterns,url
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = patterns(
    '',
    url(r'^$', views.BadgeListView.as_view(), name='badges_list'),
    url(r'^create/$', views.BadgeCreateView.as_view(), name='badge_create'),
    url(r'^(?P<pk>\d+)/$', views.BadgeUpdateView.as_view(), name='badge_detail'),
    url(r'^(?P<pk>\d+)/delete/$', views.BadgeDeleteView.as_view(), name='badge_delete'),
    url(r'^create/batch/$', 'badges.views.batch', name='badges_batch'),
    url(r'^view/(?P<term>(Fa|Sp)\d{2})/$', views.BadgeTermView.as_view(), name='badges_term'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 