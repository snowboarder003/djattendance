from django.contrib import admin
from ap.accounts.models import UserAccount

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserAccount, UserAdmin)
