# Generated by Django 3.2.5 on 2022-08-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0008_alter_noticia_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
