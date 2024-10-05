from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    class Meta:
        model = User
        fields = '__all__'

# Register the custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
