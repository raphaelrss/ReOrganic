import re

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff = is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True, help_text=_('Required. 15 characters or fewer.Letters, numbers and @/./ + / - /_ characters'),
                                validators=[validators.RegexValidator(re.compile('^[\w. @+-]+$'), _('Enter a valid username.'), _('invalid'))])
    first_name = models.CharField(_('firstname'), max_length=30)
    last_name = models.CharField(_('lastname'), max_length=30)
    email = models.EmailField(_('emailaddress'), max_length=255, unique = True)
    is_staff = models.BooleanField(_('staffstatus'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default = True,
    help_text = _('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('datejoined'), default = timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default = False,
        help_text = _('Designates whether this user has confirmed his account.'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = ' %s % s' %(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    numero = models.IntegerField()
    cep = models.CharField(max_length=8)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)


class Compost(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class Post(models.Model):
    responsavel_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()


class Entrega(models.Model):
    responsavel_id = models.ForeignKey(Compost, on_delete=models.CASCADE)
    descricao = models.TextField()


class Coleta(models.Model):
    responsavel_id = models.ForeignKey(Compost, on_delete=models.CASCADE)
    descricao = models.TextField()


class Troca(models.Model):
    coleta_id = models.ForeignKey(Coleta, on_delete=models.CASCADE)
    entrega_id = models.ForeignKey(Entrega, on_delete=models.CASCADE)
    data_troca = models.DateTimeField(auto_created=True)


class Avaliacao(models.Model):
    troca_id = models.ForeignKey(Troca, on_delete=models.CASCADE)
    responsavel_id = models.ForeignKey(Compost, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    descricao = models.TextField()

