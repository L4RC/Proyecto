from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

admin.site.register(CustomUser)
