# Generated by Django 2.2.3 on 2020-11-09 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name_plural': 'Respuestas'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name_plural': 'Lecciones'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AlterModelOptions(
            name='studentresponses',
            options={'verbose_name_plural': 'Respuestas de estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='userextend',
            options={'verbose_name_plural': 'Perfil usuario'},
        ),
    ]
