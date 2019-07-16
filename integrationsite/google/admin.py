from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
UserAdmin.fieldsets += ('Extra Information', {'fields': ('bio', 'birth_date', 'location')}),

admin.site.register(User, UserAdmin)
