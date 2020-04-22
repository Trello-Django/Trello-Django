from django.db import models
# from django.contrib.postgres.fields import ArrayField
from my_auth.models import MyUser
import datetime

class Board(models.Model):
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='boards_owner')
    reviewer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='boards_reviwer')

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'boards'
    def __str__(self):
        return f'Board:{self.title}, owner:{self.owner}, reviewer:{self.reviewer}'

class List(models.Model):
    title = models.CharField(max_length=300)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')

    class Meta:
        verbose_name = 'list'
        verbose_name_plural = 'lists'


class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    dueDate = models.DateTimeField(default= datetime.datetime.now() + datetime.timedelta(days=7))
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'




