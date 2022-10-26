from django.db import models

# Create your models here.


class InstaPhoto(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='upload/')

