# Generated by Django 4.2.7 on 2023-11-20 19:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 15 characters or fewer.Letters, numbers and @/./ + / - /_ characters', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w. @+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='firstname')),
                ('last_name', models.CharField(max_length=30, verbose_name='lastname')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='emailaddress')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staffstatus')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datejoined')),
                ('is_trusty', models.BooleanField(default=False, help_text='Designates whether this user has confirmed his account.', verbose_name='trusty')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('responsavel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compost')),
            ],
        ),
        migrations.CreateModel(
            name='Troca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_troca', models.DateTimeField(auto_created=True)),
                ('coleta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.coleta')),
                ('entrega_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.entrega')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('conteudo', models.TextField()),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('responsavel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compost',
            name='endereco_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.endereco'),
        ),
        migrations.AddField(
            model_name='compost',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coleta',
            name='responsavel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compost'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
                ('responsavel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compost')),
                ('troca_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.troca')),
            ],
        ),
    ]
