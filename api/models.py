from django.db import models

# Create your models here.

class Action(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='something')

    def __str__(self):
        return self.text