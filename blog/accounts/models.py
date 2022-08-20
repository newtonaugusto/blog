
import re

from typing import Optional

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    Group, UserManager as AbstractUserManager)
from django.core import validators
from django.db import models


class UserManager(AbstractUserManager, models.Manager):

    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_superuser(self, email: Optional[str],
                         password: Optional[str], **extra_fields):
        return super().create_superuser(email, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de Usuário', max_length=100, unique=True,
        validators=[validators.RegexValidator(
            re.compile('^[\\w.@+-]+$'),
            'O nome de usuário só pode conter letras, dígitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True, blank=True, null=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    is_superuser = models.BooleanField("É super usuário?", default=False)
    groups = models.ManyToManyField(
        Group, verbose_name="Grupo de permissões", related_name="users")
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.username, )

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
