# Generated by Django 3.2.5 on 2022-08-18 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0006_alter_comentario_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
    ]
