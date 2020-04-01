from django.db import models
# from django.contrib.postgres.fields import ArrayField
from my_auth.models import MyUser

class Board(models.Model):
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='boards_owner')
    # team = Асем тупой не смогла сделать = models.ManytoManyField()
    reviewer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='boards_reviwer')

class List(models.Model):
    title = models.CharField(max_length=300)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    dueDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)




