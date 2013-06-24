from django.contrib import admin

#enable manage ss in admin panel#
from ss.models import serviceCategory
from ss.models import service


admin.site.register(serviceCategory)