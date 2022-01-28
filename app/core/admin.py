from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
# underscore is the convention for converting strings
# to human readeable text
from django.utils.translation import gettext as _
# The underscore it makes easier configure more than one language


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (  # Define sections for fieldsets
        # param1=Title of the section, param2=fields
        (None, {'fields': ('email', 'password')}),
        # The comma it's when you use one field this tell django
        # that this it doesn't a string
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            # classes assigned to the form
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


#  Register in Django Admin
admin.site.register(models.User, UserAdmin)
# It doesn't need to specify the class because
# it's use the default one of the model
admin.site.register(models.Tag)
