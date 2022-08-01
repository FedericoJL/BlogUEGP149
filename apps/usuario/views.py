from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuario', default='usuario/default_user.png' )
    email = models.EmailField(null = False, blank = False)
    facebook = models.URLField(null = True, blank = True)
    twitter = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)
