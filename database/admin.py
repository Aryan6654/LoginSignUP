from django.contrib import admin
from django.db import models
from .models import User2

# Register your models here.
@admin.register(User2)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'password')