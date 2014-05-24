from django.conf.urls import patterns, url

from mealSeating import views

urlpatterns = patterns('',
    # url(r'^$', views.seating, name='detail'),
    url(r'viewList/brothers/$',
        views.brothertables),
    url(r'viewList/sisters/$',
        views.sistertables)
)
