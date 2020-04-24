from django.db import models
from my_auth.models import MyUser
from core.models import Board


class TeamManager(models.Manager):
    pass


class Team(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now=True, editable=False, null=False)
    board = models.OneToOneField(Board, on_delete=models.CASCADE, related_name='team')
    objects = TeamManager()

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return f'Team: {self.name}'


class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    PRODUCT = 'PM'
    DEVELOPER = 'DEV'
    REVIEWER = 'R'
    ROLES = (
        (PRODUCT, 'PRODUCT_MANAGER'),
        (DEVELOPER, 'DEVELOPER'),
        (REVIEWER, 'REVIEWER'),
    )
    avatar = models.ImageField(upload_to='profile_images', null=True)
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    date_of_birth = models.DateField(null=True, editable=True, auto_now=False)
    phone = models.CharField(max_length=255, null=True, default='')
    role = models.CharField(choices=ROLES, default=DEVELOPER, null=False, max_length=255)
    user = models.OneToOneField(MyUser, null=False, on_delete=models.CASCADE, related_name='profile')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    objects = ProfileManager()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'Profile: {self.name} {self.surname}'
