# Generated by Django 3.2.5 on 2022-08-20 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0019_alter_noticia_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='destacada',
        ),
    ]