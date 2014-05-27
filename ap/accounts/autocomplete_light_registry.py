import autocomplete_light
from models import Trainee

autocomplete_light.register(Trainee,
	# Just like in ModelAdmin.search_fields
	search_fields=['^account__firstname', '^account__nickname', '^account__lastname'],
)