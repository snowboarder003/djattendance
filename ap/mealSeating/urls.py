from django.conf.urls import patterns, url

from mealSeating import views

urlpatterns = patterns('',
    url(r'newSeating/',
        views.newseats),
    url(r'viewList/',
        views.seattables),
    url(r'mealsignin/',
        views.signin),
)
