# Generated by Django 3.2.5 on 2022-08-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0021_alter_noticia_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]