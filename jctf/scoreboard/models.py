from django.db import models

class User(models.Model):
  """ User Model. The User is CTF Player """
  name = models.CharField(max_length=140)
  email = models.EmailField(unique=False)

  def __str__(self):
    return self.name


