from django.db import models
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  filename = models.CharField(max_length=255)
# Create your models here.
