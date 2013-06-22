from django.conf.urls import patterns, url

from terms import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<code>(Fa|Sp)\d{2})/$', views.TermDetailView.as_view(), name='detail'),
    url(r'^add_term.html$', views.AddTermView.as_view(), name='add_term'),
    url(r'^(?P<code>(Fa|Sp)\d{2})/delete/$', views.DeleteTermView.as_view(), name='delete_term'),
)                    
