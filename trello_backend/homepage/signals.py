from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from my_auth.models import MyUser
from .models import Profile, Team

@receiver(post_save, sender = MyUser)
def user_created(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance)
    print("OKOKOK")

@receiver(post_delete, sender = Profile)
def profile_deleted(sender, instance, **kwargs):
    team_id = instance.team
    team = Team.objects.get(id=team_id)
    if team.profile_set.count() == 0:
        team.delete()
        print("ok")

