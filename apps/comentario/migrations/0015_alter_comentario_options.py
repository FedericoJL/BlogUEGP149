# Generated by Django 3.2.5 on 2022-08-20 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0014_alter_comentario_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-fecha']},
        ),
    ]