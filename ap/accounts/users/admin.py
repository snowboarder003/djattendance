from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import UserAccount

# Define an inline admin descriptor for UserAccount model
# which acts like a singleton
class UserInline(admin.StackedInline):
    model = UserAccount
    can_delete = False
    verbose_name_plural = 'user'

# Define a new User Admin
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
