from django.db import models
# from django.contrib.postgres.fields import ArrayField
from my_auth.models import MyUser
import datetime


class BoardManager(models.Manager):
    pass

class BoardStatusCountManager(models.Manager):
    def status_count(self, status):
        return self.filter(status=status).count()

class Board(models.Model):
    STATUSES = (
        (1, 'ACTIVE'),
        (2, 'CLOSED')
    )
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    status = models.IntegerField(choices=STATUSES, default=1)

    objects = BoardManager()
    status_count = BoardStatusCountManager()

    class Meta:
        verbose_name = 'core'
        verbose_name_plural = 'boards'

    def __str__(self):
        return f'Board:{self.title}'

class Listmanager(models.Manager):
    pass

class List(models.Model):
    title = models.CharField(max_length=300)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    on_review = models.BooleanField(default=True)

    objects = Listmanager()

    class Meta:
        verbose_name = 'list'
        verbose_name_plural = 'lists'

    def __str__(self):
        return f'List: {self.title}'

class TaskManager(models.Manager):
    def for_owner(self):
        return self.filter(owner = self.request.user)


class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    dueDate = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=7))
    created_at = models.DateTimeField(auto_now_add=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    attachment = models.FileField(upload_to='attachments', null=True, blank=True)
    image = models.ImageField(upload_to='task_images', null=True, blank=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='task_owner')
    assigned = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='task_assigner', default=1)
    completed = models.BooleanField(default=False)

    objects = TaskManager()

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
         return f'Task:{self.title}, {self.description}, due: {self.dueDate}, owner:{self.owner.username}'





