from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Board,List

@receiver(post_save, sender = Board)
def board_created(sender, instance, created, **kwargs):
    List.objects.create(board=instance, title = 'TODO')
    List.objects.create(board=instance, title = 'IN_PROGRESS')
    List.objects.create(board=instance, title = 'REVIEW')
    List.objects.create(board=instance, title = 'DONE')
