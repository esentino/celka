from django.db import models

class History(models.Model):
    value = models.IntegerField()
