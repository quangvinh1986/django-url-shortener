from django.db import models


class MyURL(models.Model):
    alias = models.CharField(max_length=200)
    url = models.CharField(max_length=5000)
