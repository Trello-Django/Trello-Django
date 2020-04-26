from django.core.management.base import BaseCommand, CommandError
from core.models import Task, List, Board

class Command(BaseCommand):
    help = 'Delete objects'

    def add_arguments(self, parser):
        parser.add_argument('titles', nargs = '+', type=str, help = 'Titles of objects to delete')


    def handle(self, *args, **kwargs):
        titles = kwargs.get('titles')

        for title in titles:
            try:
                task = Task.objects.get(title=title)
            except Task.DoesNotExist:
                raise CommandError(f'Task {task.title} does not exist')

            task.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {task.title}'))


