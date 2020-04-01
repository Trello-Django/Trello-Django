from django.contrib import admin
from .models import Board, List, Task

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','title','owner','reviewer',)
    search_fields = ('title',)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title','board',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','dueDate','created_at','owner','list',)




