# Generated by Django 4.0.6 on 2022-07-27 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colunista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Colunistas',
            },
        ),
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('data_pub', models.DateTimeField(auto_now_add=True)),
                ('colunista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.colunista')),
            ],
            options={
                'verbose_name_plural': 'Edições',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('colunista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.colunista')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.edicao')),
            ],
            options={
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('colunista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.colunista')),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.noticia')),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
