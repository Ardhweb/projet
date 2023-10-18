from django.contrib import admin

# Register your models here.
from .models import User

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['password']

