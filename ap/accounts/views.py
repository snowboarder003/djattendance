from django.http import HttpResponse
from accounts.models import APUserManager

def index(request):
	return HttpResponse("Hello, world. You're at the polls index")
	##loginUser = APUserManager.create_user('lifeunion@gmail.com', '123456')


