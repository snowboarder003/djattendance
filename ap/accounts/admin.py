from django.contrib import admin
from accounts.models import *

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount, UserAdmin)
admin.site.register(TrainingAssistant)
admin.site.register(Trainee)
