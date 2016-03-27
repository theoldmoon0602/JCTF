from django.db import models
from django.core.validators import URLValidator

class Hint(models.Model):
    """ Hints are Belong to one Problem. """
    name = models.CharField(max_length=128)
    text = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class User(models.Model):
    """ User Model. The User is CTF Player """
    name = models.CharField(max_length=140, unique=True)
    email = models.EmailField(unique=False)
    used_hints = models.ManyToManyField(Hint, blank=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    """ Problems. Containing problem text and ... """
    name = models.CharField(max_length=256, unique=True)
    flag = models.CharField(max_length=256, unique=True)
    point = models.IntegerField()
    text = models.TextField(blank=True,)
    url = models.TextField(validators=[URLValidator()], blank=True)
    solvedby = models.ManyToManyField(User, blank=True)
    hint = models.ManyToManyField(Hint, blank=True)

    def __str__(self):
        return self.name
