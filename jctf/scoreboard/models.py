from django.db import models
from django.core.validators import URLValidator


class User(models.Model):
    """ User Model. The User is CTF Player """
    name = models.CharField(max_length=140, unique=True)
    email = models.EmailField(unique=False)

    def __str__(self):
        return self.name


class Hint(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=256, unique=True)
    text = models.TextField()
    url = models.TextField(validators=[URLValidator()], blank=True)
    solvedby = models.ManyToManyField(User, blank=True)
    hint = models.ManyToManyField(Hint, blank=True)

    def __str__(self):
        return self.name
