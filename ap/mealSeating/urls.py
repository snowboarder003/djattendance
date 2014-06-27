from django.conf.urls import patterns, url

from mealSeating import views

urlpatterns = patterns('',
    # url(r'^$', views.seating, name='detail'),
    url(r'viewList/',
        views.seattables),
     url(r'newSeating/',
        views.newseats)
    # url(r'viewList/sisters/$',
    #      views.seattables)
)
