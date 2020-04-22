from django.contrib import admin
from .models import Board, List, Task

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','title','status', 'created_at')
    search_fields = ('title',)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title','board','on_review')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','dueDate','created_at','list','owner','assigned')




