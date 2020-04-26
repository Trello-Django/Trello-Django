from django.contrib import admin
from .models import Profile,Team

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','phone','role','user',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','board')