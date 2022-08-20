# Generated by Django 3.2.5 on 2022-08-18 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentario', '0007_remove_comentario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='usuario.usuario'),
            preserve_default=False,
        ),
    ]
