from django.conf.urls import patterns, url

from mealSeating import views

urlpatterns = patterns('',
    # url(r'^$', views.seating, name='detail'),
    url(r'viewList/(?P<gender>[A-Z]{1})/$',
        views.seattables),
    # url(r'viewList/sisters/$',
    #      views.seattables)
)
