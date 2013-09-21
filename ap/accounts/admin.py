from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User

"""" ACCOUNTS admin.py """

class APUserCreationForm(forms.ModelForm):
    """ A form for creating a new user """

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_repeat = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "firstname", "lastname")

    def clean_password(self):
        """ Check that the password match """
        password = self.cleaned_data.get("password")
        password_repeat = self.cleaned_data.get("password_repeat")
        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError("Password's don't match")
        return password_repeat

    def save(self, commit=True):
        """ Save the provided password in hashed format """
        user = super(APUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class APUserChangeForm(forms.ModelForm):
    """ A form for updating users. """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        return self.initial["password"]


class APUserAdmin(UserAdmin):
    # Set the add/modify forms
    add_form = APUserCreationForm
    form = APUserChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin that reference specific fields on auth.User
    list_display = ("email", "is_staff", "firstname", "lastname")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "firstname", "lastname")
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        (None, {"fields": 
                            ("email", "password")}),
        ("Personal info", {"fields": 
                            ("firstname", "lastname")}),
        ("Permissions", {"fields": 
                            ("is_active",
                            "is_staff",
                            "is_superuser",
                            "groups",
                            "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "firstname", "lastname", "password", "password_repeat")}
        ),
    )

# Register the new Admin
admin.site.register(User, APUserAdmin)


