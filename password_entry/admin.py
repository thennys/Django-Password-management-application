from django.contrib import admin

#Register your models here.
from .models import CustomUser, PasswordEntry

admin.site.register(CustomUser)
admin.site.register(PasswordEntry)
