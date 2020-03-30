from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, UserManager, PermissionsMixin


class MyUserManager(UserManager):
    pass


class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=False, unique=True)
    first_name = models.CharField(max_length=255, null=False,)
    second_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True


class MyUser(MyAbstractUser):
    pass
