from django.conf.urls import patterns, url
from verse_parse import views
#from verse_parse.preview import FileFormPreview
#from verse_parse.forms import DisplayForm

urlpatterns = patterns('',
	url(r'^$', views.upload_file, name='verse_parse'),
	#url(r'^post/$', FileFormPreview(DisplayForm)),
)