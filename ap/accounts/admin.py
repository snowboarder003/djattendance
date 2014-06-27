from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import Group, User

from accounts.models import User, Trainee, TrainingAssistant
from aputils.admin import VehicleInline, EmergencyInfoInline

"""" ACCOUNTS admin.py """

class APUserCreationForm(forms.ModelForm):
    """ A form for creating a new user """

    password = forms.CharField(label="Password", 
                               widget=forms.PasswordInput)
    password_repeat = forms.CharField(label="Password confirmation", 
                                      widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "firstname", "lastname")

    def clean(self):
        cleaned_data = super(APUserCreationForm, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        if password != password_repeat:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def save(self, commit=True):
        """ Save the provided password in hashed format """
        user = super(APUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class APUserChangeForm(forms.ModelForm):
    """ A form for updating users. """

    class Meta:
        model = User
        exclude = ['password']
    

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
                            ("email",)}),

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
    

class TraineeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            # add 'bunk' back in once db behaves
            'fields': (('account', 'active',), 'type', 'term', ('date_begin', 'date_end',), ('married', 'spouse',), ('TA', 'mentor',), 'team', 'house', 'address', 'self_attendance',)
        }),
    )
    list_display = ('__unicode__', 'current_term')
    inlines = [
        VehicleInline,
        EmergencyInfoInline,    
    ]
    
    """
	#overriding save function to add user to house_coordinator group if applicable
	def save_model(self, request, obj, form, change):
        
        if commit:
        	#if user is a house_coordinator, adds user to the house_coordinator group
        	if obj.user.profile.trainee.house_coordinator:
        		try:
        			group = Group.objects.get(name='house_coordinator')
        			group.user_set.add(obj.user)
        		else:
        			group = Group.objects.create(name = 'house_coordinator')
            user.save()
        return user
"""


# Register the new Admin
admin.site.register(User, APUserAdmin)
admin.site.register(Trainee, TraineeAdmin)
admin.site.register(TrainingAssistant)
